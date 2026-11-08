export function initialize(frame) {
  const toolbar = frame.querySelector("[data-pv-toolbar]");
  const main = frame.querySelector(".pv-main");
  const options = [...main.querySelectorAll(".pv-option")];
  const details = [...toolbar.querySelectorAll("[data-pv-detail]")];
  const actions = [...toolbar.querySelectorAll("[data-pv-panel-toggle]")];
  const panels = [...toolbar.querySelectorAll("[data-pv-panel]")];
  const expanded = toolbar.querySelector("[data-pv-expanded]");
  const handle = toolbar.querySelector("[data-pv-drag]");
  const selection = toolbar.querySelector("[data-pv-select]");
  const knobCount = toolbar.querySelector("[data-pv-knob-count]");
  const reducedMotion = matchMedia("(prefers-reduced-motion: reduce)");
  const animations = new Set();
  let pendingUpdate;
  let panelAnimation;
  let activePanel = null;
  let selected = options[0];
  let moved = false;

  function clearMotion() {
    for (const animation of animations) animation.cancel();
    animations.clear();
    pendingUpdate = undefined;
  }

  function pieces(option) {
    const marked = [...option.querySelectorAll("[data-pv-piece]")];
    const roots = marked.length > 0
      ? marked.filter(element => !element.parentElement.closest("[data-pv-piece]"))
      : [...option.querySelector(".pv-page").children];
    return roots.flatMap(movingPieces);
  }

  function animatePiece(piece, keyframes, duration, delay, finish) {
    const animation = piece.animate(keyframes, {
      duration, delay, fill: "both", easing: "cubic-bezier(.2,.7,.2,1)",
    });
    animations.add(animation);
    animation.onfinish = finish ?? (() => {
      animation.cancel();
      animations.delete(animation);
    });
  }

  function transition(update) {
    clearMotion();
    if (!selected || reducedMotion.matches) {
      update();
      return;
    }
    pendingUpdate = update;
    const outgoing = pieces(selected);
    let remaining = outgoing.length;
    if (remaining === 0) {
      enter();
      return;
    }

    outgoing.forEach((piece, index) => {
      const travel = 32 + Math.min(index, 4) * 4;
      animatePiece(piece, [
        { transform: "translateY(0)", opacity: 1 },
        { transform: `translateY(${-travel}px)`, opacity: 0 },
      ], 92, index * 5, () => {
        remaining -= 1;
        if (remaining !== 0) return;
        enter();
      });
    });
  }

  function enter() {
    const update = pendingUpdate;
    clearMotion();
    update();
    if (reducedMotion.matches) return;

    pieces(selected).forEach((piece, index) => {
      const travel = 36 + Math.min(index, 4) * 4;
      animatePiece(piece, [
        { transform: `translateY(${travel}px)`, opacity: 0 },
        { transform: "translateY(0)", opacity: 1 },
      ], 104, index * 6);
    });
  }

  function moveTo(left, top) {
    const bounds = toolbar.getBoundingClientRect();
    const maxLeft = Math.max(0, window.innerWidth - bounds.width);
    const maxTop = Math.max(0, window.innerHeight - bounds.height);

    toolbar.style.left = `${Math.min(maxLeft, Math.max(0, left))}px`;
    toolbar.style.top = `${Math.min(maxTop, Math.max(0, top))}px`;
    toolbar.style.bottom = "auto";
    frame.dataset.pvMoved = "";
    moved = true;
  }

  function clampPosition() {
    if (!moved) return;
    moveTo(toolbar.offsetLeft, toolbar.offsetTop);
  }

  function resizePanel(update) {
    const height = expanded.getBoundingClientRect().height;
    panelAnimation?.cancel();
    expanded.hidden = activePanel === null;
    update();
    const target = expanded.getBoundingClientRect().height;
    if (height === target || reducedMotion.matches) {
      clampPosition();
      return;
    }

    const animation = expanded.animate([
      { height: `${height}px`, overflow: "hidden" },
      { height: `${target}px`, overflow: "hidden" },
    ], { duration: 88, easing: "cubic-bezier(.2,.7,.2,1)" });
    panelAnimation = animation;
    animation.onfinish = () => {
      animation.cancel();
      panelAnimation = undefined;
      clampPosition();
    };
  }

  function renderSelection(option) {
    selected = option;
    for (const candidate of options) candidate.hidden = candidate !== option;
    for (const detail of details) detail.hidden = detail.dataset.pvDetail !== option.id;
    selection.value = option.id;

    const detail = details.find(candidate => candidate.dataset.pvDetail === option.id);
    const knobs = detail ? countKnobs(detail) : 0;
    knobCount.textContent = String(knobs);
    knobCount.hidden = knobs === 0;
    clampPosition();
  }

  function select(id) {
    const option = options.find(candidate => candidate.id === id);
    if (!option) return;
    if (option === selected) {
      clearMotion();
      renderSelection(option);
      history.replaceState(null, "", `#${id}`);
      return;
    }

    transition(() => resizePanel(() => renderSelection(option)));
    history.replaceState(null, "", `#${id}`);
  }

  function togglePanel(id) {
    const height = expanded.getBoundingClientRect().height;
    panelAnimation?.cancel();
    expanded.hidden = false;
    activePanel = activePanel === id ? null : id;
    const open = activePanel !== null;
    for (const action of actions) {
      action.setAttribute("aria-expanded", String(action.dataset.pvPanelToggle === activePanel));
    }
    for (const panel of panels) panel.hidden = panel.dataset.pvPanel !== id;
    frame.dataset.pvOpen = String(open);
    const target = open ? expanded.getBoundingClientRect().height : 0;
    if (reducedMotion.matches) {
      expanded.hidden = !open;
      clampPosition();
      return;
    }

    const animation = expanded.animate([
      { height: `${height}px`, paddingTop: height > 0 ? "16px" : "0",
        paddingBottom: height > 0 ? "16px" : "0", overflow: "hidden" },
      { height: `${target}px`, paddingTop: open ? "16px" : "0",
        paddingBottom: open ? "16px" : "0", overflow: "hidden" },
    ], { duration: 88, fill: "both", easing: "cubic-bezier(.2,.7,.2,1)" });
    panelAnimation = animation;
    animation.onfinish = () => {
      expanded.hidden = !open;
      animation.cancel();
      panelAnimation = undefined;
      clampPosition();
    };
  }

  toolbar.addEventListener("click", event => {
    const step = event.target.closest("[data-pv-step]");
    if (step && !step.disabled) stepSelect(step);
    const action = event.target.closest("[data-pv-panel-toggle]");
    if (action && !action.disabled) togglePanel(action.dataset.pvPanelToggle);
  });
  selection.addEventListener("change", event => select(event.target.value));
  toolbar.querySelector("[data-pv-navigation]").addEventListener("change", event => {
    window.location.assign(event.target.value);
  });
  for (const detail of details) {
    detail.addEventListener("input", () => queueMicrotask(() => {
      const update = pendingUpdate ?? (() => {});
      transition(update);
    }));
  }
  window.addEventListener("hashchange", () => select(location.hash.slice(1)));
  reducedMotion.addEventListener("change", () => {
    if (!reducedMotion.matches) return;
    const update = pendingUpdate;
    clearMotion();
    if (update) update();
    panelAnimation?.cancel();
    panelAnimation = undefined;
    expanded.hidden = activePanel === null;
    clampPosition();
  });

  handle.addEventListener("pointerdown", event => {
    if (event.button !== 0) return;
    event.preventDefault();
    handle.focus();
    const origin = {
      x: event.clientX, y: event.clientY,
      left: toolbar.offsetLeft, top: toolbar.offsetTop,
    };
    handle.setPointerCapture(event.pointerId);

    function drag(pointer) {
      moveTo(origin.left + pointer.clientX - origin.x, origin.top + pointer.clientY - origin.y);
    }
    function finish() {
      handle.removeEventListener("pointermove", drag);
      handle.removeEventListener("pointerup", finish);
      handle.removeEventListener("pointercancel", finish);
      handle.removeEventListener("lostpointercapture", finish);
    }
    handle.addEventListener("pointermove", drag);
    handle.addEventListener("pointerup", finish);
    handle.addEventListener("pointercancel", finish);
    handle.addEventListener("lostpointercapture", finish);
  });
  handle.addEventListener("keydown", event => {
    const movement = {
      ArrowLeft: [-16, 0], ArrowRight: [16, 0], ArrowUp: [0, -16], ArrowDown: [0, 16],
    }[event.key];
    if (!movement) return;
    event.preventDefault();
    moveTo(toolbar.offsetLeft + movement[0], toolbar.offsetTop + movement[1]);
  });
  window.addEventListener("resize", clampPosition);
  new ResizeObserver(clampPosition).observe(toolbar);

  const requested = options.find(option => option.id === location.hash.slice(1));
  const initial = requested ?? selected;
  if (initial) renderSelection(initial);
}

function movingPieces(element) {
  if (element.matches("[data-pv-still], script, style")) return [];
  if (!element.querySelector("[data-pv-still]")) return [element];
  return [...element.children].flatMap(movingPieces);
}

// A radio group shares one name, so each distinct name is one knob.
function countKnobs(detail) {
  const controls = [...detail.querySelectorAll("input, select, textarea")];
  const named = new Set(controls.filter(control => control.name).map(control => control.name));
  const unnamed = controls.filter(control => !control.name);
  return named.size + unnamed.length;
}

function stepSelect(button) {
  const select = button.closest("[data-pv-stepper]").querySelector("select");
  const count = select.options.length;

  select.selectedIndex = (select.selectedIndex + Number(button.dataset.pvStep) + count) % count;
  select.dispatchEvent(new Event("change", { bubbles: true }));
}

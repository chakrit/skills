import Mock from "./Mock.astro";
import Knobs from "./Knobs.astro";

export const meta = {
  group: "Phase 1 · Controls",
  title: "Control shape",
  note: "Round 1 · Starter examples",
  building: true,
  questions: [],
  notes: [
    { id: "example-N1", text: "Compare the control corners on the same mock." },
  ],
};

export const options = [
  {
    id: "A",
    name: "Square",
    note: "Straight corners",
    width: "28rem",
    component: Mock,
    props: { radius: "0" },
  },
  {
    id: "B",
    name: "Rounded",
    note: "Adjust the corner radius",
    width: "28rem",
    component: Mock,
    props: { radius: "0.5rem" },
    sidebar: Knobs,
    sidebarProps: { slug: "example", option: "B" },
  },
];

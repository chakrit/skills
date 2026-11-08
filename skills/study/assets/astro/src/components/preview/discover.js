export async function discover(loaders, indexHref) {
  const entries = Object.entries(loaders).filter(([path]) => !path.endsWith("/index.astro"));
  const previews = await Promise.all(entries.map(async ([path, loader]) => {
    const slug = path.split("/").at(-1).slice(0, -6);
    const href = `${indexHref}${slug}/`;

    try {
      const { meta } = await loader();
      if (typeof meta?.group !== "string" || !meta.group.trim()) {
        throw new Error(`${slug} must export a nonempty meta.group`);
      }
      if (typeof meta?.title !== "string" || !meta.title.trim()) {
        throw new Error(`${slug} must export a nonempty meta.title`);
      }
      return { ...meta, href };
    } catch (error) {
      console.error(`Study preview failed: ${slug}`, error);
      return { href, group: "Broken right now", title: slug, broken: String(error) };
    }
  }));

  return previews.sort((a, b) => a.group.localeCompare(b.group, "en", { numeric: true }));
}

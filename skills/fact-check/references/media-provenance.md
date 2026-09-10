# Media Provenance & Forensics

Read this when a claim rests on an image, video, or audio clip — verify the *media* before
the claim. Synthetic and recycled media is now a dominant disinformation vector: tracked
deepfake incidents rose roughly 900% from 2023 to 2025.

## First moves
- **Reverse image search across engines** — run Google, Yandex (strongest for faces and
  places), and TinEye in parallel; they index different corpora. Look for earlier
  appearances: a "breaking" image with a years-old footprint is recycled.
- **Trace to origin** — find the earliest, highest-resolution copy and its original
  caption and context. Crop-and-recaption is the cheapest manipulation there is.

## Provenance signals
- **C2PA / Content Credentials** — check for embedded provenance: who created the file,
  when, with what tool, whether AI was involved, and the edit history. Backed by Adobe,
  Google, Meta, OpenAI, Sony, Nikon, and Leica, and CISA-endorsed. **Caveat:** C2PA proves
  *origin and edit history, not truth*. Absence of credentials proves nothing, and their
  presence only tells you the recorded history. Treat it as one input, not a verdict.
- **Generation watermarks** — SynthID and similar schemes may flag AI-generated output;
  absence of a watermark is not proof of authenticity.

## Geolocation & chronolocation
- **Geolocation** — match landmarks, signage, language, architecture, and terrain against
  maps and street-level imagery to confirm *where*.
- **Chronolocation** — use shadow direction and length against solar position (SunCalc,
  Bellingcat's Shadow Finder) plus weather records to confirm *when*; this rules out
  backdated or spoofed timing.

## Red flags
Inconsistent lighting or shadows, warped edges or hands, mismatched reflections, audio-lip
desync, metadata stripped or inconsistent with the claimed origin, and any version whose
earliest traceable appearance predates the claimed event.

> Provenance and forensics establish whether the media is what it claims to be. They do
> not establish that the underlying real-world claim is true — fold the result back into
> the SIFT process in `SKILL.md`.

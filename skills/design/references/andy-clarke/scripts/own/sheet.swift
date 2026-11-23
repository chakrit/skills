// Make a 2x2 contact sheet of the top part of up to four PNGs, with labels.
// Usage: swift sheet.swift <out.png> <cropHeight> <img1> [img2 img3 img4]
import AppKit
let a = CommandLine.arguments
let out = a[1]; let cropH = CGFloat(Double(a[2])!)
let files = Array(a[3...])
let cellW: CGFloat = 700, cellH: CGFloat = cropH / 2
let sheet = NSImage(size: NSSize(width: cellW*2, height: (cellH+24)*2))
sheet.lockFocus()
NSColor.white.setFill(); NSRect(x: 0, y: 0, width: cellW*2, height: (cellH+24)*2).fill()
for (i, f) in files.enumerated() {
  guard let img = NSImage(contentsOfFile: f), let rep = img.representations.first else { continue }
  let w = CGFloat(rep.pixelsWide), h = CGFloat(rep.pixelsHigh)
  let scale = img.size.width / w
  let srcH = min(cropH, h)
  let src = NSRect(x: 0, y: (h - srcH) * scale, width: min(1400, w) * scale, height: srcH * scale)
  let col = CGFloat(i % 2), row = CGFloat(1 - i / 2)
  let dst = NSRect(x: col*cellW, y: row*(cellH+24), width: cellW, height: srcH/2)
  let dstTop = NSRect(x: dst.minX, y: row*(cellH+24) + (cellH - srcH/2), width: dst.width, height: dst.height)
  img.draw(in: dstTop, from: src, operation: .copy, fraction: 1)
  let label = (f as NSString).lastPathComponent as NSString
  label.draw(at: NSPoint(x: col*cellW + 6, y: row*(cellH+24) + cellH + 4), withAttributes: [.font: NSFont.boldSystemFont(ofSize: 16), .foregroundColor: NSColor.red])
}
sheet.unlockFocus()
let rep = NSBitmapImageRep(data: sheet.tiffRepresentation!)!
try! rep.representation(using: .png, properties: [:])!.write(to: URL(fileURLWithPath: out))

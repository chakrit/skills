// Extract text and render pages of a PDF. Usage: swift pdf.swift <in.pdf> <outdir> <scale>
import Foundation
import PDFKit
import AppKit
let args = CommandLine.arguments
let doc = PDFDocument(url: URL(fileURLWithPath: args[1]))!
let out = args[2]; let scale = CGFloat(Double(args[3]) ?? 1.0)
var text = ""
for i in 0..<doc.pageCount {
  let p = doc.page(at: i)!
  text += "\n\n=== page \(i+1)\n" + (p.string ?? "")
  let r = p.bounds(for: .mediaBox)
  let size = NSSize(width: r.width*scale, height: r.height*scale)
  let img = p.thumbnail(of: size, for: .mediaBox)
  if let tiff = img.tiffRepresentation, let rep = NSBitmapImageRep(data: tiff),
     let png = rep.representation(using: .png, properties: [:]) {
    try! png.write(to: URL(fileURLWithPath: "\(out)/page-\(String(format: "%02d", i+1)).png"))
  }
}
try! text.write(toFile: "\(out)/text.txt", atomically: true, encoding: .utf8)
print(doc.pageCount)

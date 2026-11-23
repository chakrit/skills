// Crop a vertical band from a PNG. Usage: swift crop.swift <in.png> <out.png> <y> <height>
import AppKit
let a = CommandLine.arguments
let rep = NSBitmapImageRep(data: try! Data(contentsOf: URL(fileURLWithPath: a[1])))!
let y = Int(a[3])!, h = min(Int(a[4])!, rep.pixelsHigh - Int(a[3])!)
let cg = rep.cgImage!.cropping(to: CGRect(x: 0, y: y, width: rep.pixelsWide, height: h))!
let out = NSBitmapImageRep(cgImage: cg)
try! out.representation(using: .png, properties: [:])!.write(to: URL(fileURLWithPath: a[2]))

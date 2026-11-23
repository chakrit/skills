// Usage: swift pdftext.swift <in.pdf> <out.txt> <source-url>
import Foundation
import PDFKit
let a = CommandLine.arguments
guard let doc = PDFDocument(url: URL(fileURLWithPath: a[1])) else { exit(1) }
var s = a[3] + "\n"
for i in 0..<doc.pageCount { s += (doc.page(at: i)?.string ?? "") + "\n" }
try! s.write(toFile: a[2], atomically: true, encoding: .utf8)

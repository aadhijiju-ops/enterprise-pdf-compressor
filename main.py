import os
from pypdf import PdfReader, PdfWriter


def compress_pdf(input_path, output_path):
    """
    Compresses a PDF file by optimizing content streams.
    """
    # Check if the input file exists
    if not os.path.exists(input_path):
        print(f"Error: The file '{input_path}' does not exist.")
        return

    print("Compressing... This might take a moment for larger files.")

    # Read the original PDF
    reader = PdfReader(input_path)
    writer = PdfWriter()

    # Copy pages and apply lossless compression to each page's stream
    for page in reader.pages:
        page.compress_content_streams()  # Reduces text and vector graphic overhead
        writer.add_page(page)

    # Save the newly optimized PDF
    with open(output_path, "wb") as f:
        writer.write(f)

    # Calculate and display the space saved
    initial_size = os.path.getsize(input_path)
    final_size = os.path.getsize(output_path)
    saved_bytes = initial_size - final_size

    # Fixed: Correctly multiplied by 100 for the percentage calculation
    savings_percentage = (saved_bytes / initial_size) * 100 if initial_size > 0 else 0

    print(f"Success! Compressed PDF saved to: {output_path}")
    print(f"Original Size: {initial_size / 1024:.2f} KB")
    print(f"Compressed Size: {final_size / 1024:.2f} KB")
    print(f"Space Saved: {saved_bytes / 1024:.2f} KB ({savings_percentage:.1f}%)")


# Example usage:
# Replace these strings with your actual file names or paths in PyCharm
input_file = "large_document.pdf"
output_file = "compressed_document.pdf"

compress_pdf(input_file, output_file)
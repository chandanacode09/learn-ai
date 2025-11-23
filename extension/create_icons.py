#!/usr/bin/env python3
"""
Create extension icons
Simple script to generate placeholder icons for the Chrome extension
"""
from PIL import Image, ImageDraw, ImageFont
import os

def create_icon(size, output_path):
    """Create a simple brain emoji icon"""
    # Create image with gradient background
    img = Image.new('RGB', (size, size), color='white')
    draw = ImageDraw.Draw(img)

    # Draw gradient background (blue to purple)
    for y in range(size):
        r = int(102 + (118 - 102) * y / size)
        g = int(126 + (75 - 126) * y / size)
        b = int(234 + (162 - 234) * y / size)
        draw.line([(0, y), (size, y)], fill=(r, g, b))

    # Draw circle (simplified brain)
    margin = size // 8
    draw.ellipse([margin, margin, size-margin, size-margin], fill='white', outline=(102, 126, 234), width=size//20)

    # Draw simple brain pattern
    center_x, center_y = size // 2, size // 2
    radius = size // 3

    # Left hemisphere curves
    draw.arc([margin, margin, size-margin, size-margin], start=180, end=270, fill=(102, 126, 234), width=size//30)
    draw.arc([margin+size//10, margin, size-margin-size//10, size-margin], start=180, end=270, fill=(102, 126, 234), width=size//40)

    # Right hemisphere curves
    draw.arc([margin, margin, size-margin, size-margin], start=270, end=360, fill=(118, 75, 162), width=size//30)
    draw.arc([margin+size//10, margin, size-margin-size//10, size-margin], start=270, end=360, fill=(118, 75, 162), width=size//40)

    # Save
    img.save(output_path, 'PNG')
    print(f"✅ Created {output_path}")

# Create icons directory if it doesn't exist
icons_dir = os.path.join(os.path.dirname(__file__), 'icons')
os.makedirs(icons_dir, exist_ok=True)

# Create all three sizes
create_icon(16, os.path.join(icons_dir, 'icon16.png'))
create_icon(48, os.path.join(icons_dir, 'icon48.png'))
create_icon(128, os.path.join(icons_dir, 'icon128.png'))

print("\n✅ All extension icons created successfully!")
print("Icons location: extension/icons/")

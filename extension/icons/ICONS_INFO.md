# Extension Icons

## Current Status

The extension includes an SVG icon template (`icon.svg`). For the extension to work properly in Chrome, you need PNG versions.

## Quick Fix Options:

### Option 1: Use Online Converter
1. Go to https://convertio.co/svg-png/
2. Upload `icon.svg`
3. Download as PNG at sizes: 16x16, 48x48, 128x128
4. Save as `icon16.png`, `icon48.png`, `icon128.png`

### Option 2: Use ImageMagick (if installed)
```bash
cd extension/icons
convert -resize 16x16 icon.svg icon16.png
convert -resize 48x48 icon.svg icon48.png
convert -resize 128x128 icon.svg icon128.png
```

### Option 3: Use GIMP or Photoshop
1. Open `icon.svg`
2. Export as PNG at each required size
3. Save with correct filenames

## Temporary Workaround

The extension manifest is currently configured to use these icons. If they're not present, Chrome will show a default icon but the extension will still function.

To test immediately, you can:
1. Temporarily remove the icons section from `manifest.json`, OR
2. Use any 16x16, 48x48, and 128x128 PNG images as placeholders

## Icon Design
- Gradient: Blue (#667eea) to Purple (#764ba2)
- Symbol: Brain/AI representation
- Text: "AI" for recognition
- Style: Modern, clean, professional

# **Framebuffer Commands**
## **Drawing primitive shapes**
The following methods draw shapes onto the [FrameBuffer](https://docs.micropython.org/en/latest/library/framebuf.html#framebuf).
|<p> FrameBuffer function </p><p>  e.g. display.fill(c)  </p>|Description|
| :------------: | :-: |
|f.fill(*c*)|Fill the entire FrameBuffer with the specified color.|
|f.pixel(*x*, *y*[, *c*])|If *c* is not given, get the color value of the specified pixel. If *c* is given, set the specified pixel to the given color.|
|f.line(*x1*, *y1*, *x2*, *y2*, *c*)|Draw a line from a set of coordinates using the given color and a thickness of 1 pixel. The [line] method draws the line up to a second set of coordinates whereas the [hline] and [vline](https://docs.micropython.org/en/latest/library/framebuf.html#framebuf.FrameBuffer.vline) methods draw horizontal and vertical lines respectively up to a given length.|
|f.vline(*x*, *y*, *h*, *c*)||
|f.hline(*x*, *y*, *w*, *c*)||
|f.rect(*x*, *y*, *w*, *h*, *c*[, *f*])|<p>Draw a rectangle at the given location, size and color.</p><p>The optional *f* parameter can be set to True to fill the rectangle. Otherwise just a one pixel outline is drawn.</p>|
|f.ellipse(*x*, *y*, *xr*, *yr*, *c*[, *f*, *m*])|<p>Draw an ellipse at the given location. Radii *xr* and *yr* define the geometry; equal values cause a circle to be drawn. The *c* parameter defines the color.</p><p>The optional *f* parameter can be set to True to fill the ellipse. Otherwise just a one pixel outline is drawn.</p><p>The optional *m* parameter enables drawing to be restricted to certain quadrants of the ellipse. The LS four bits determine which quadrants are to be drawn, with bit 0 specifying Q1, b1 Q2, b2 Q3 and b3 Q4. Quadrants are numbered counterclockwise with Q1 being top right.</p>|
|f.poly(*x*, *y*, *coords*, *c*[, *f*])|<p>Given a list of coordinates, draw an arbitrary (convex or concave) closed polygon at the given x, y location using the given color.</p><p>The *coords* must be specified as a [array](https://docs.micropython.org/en/latest/library/array.html#module-array) of integers, e.g. array('h', [x0, y0, x1, y1, ... xn, yn]).</p><p>The optional *f* parameter can be set to True to fill the polygon. Otherwise just a one pixel outline is drawn.</p>|

## **Drawing text**
|<p>FrameBuffer function</p><p>eg display.fill(c)</p>|Description|
| :-: | :-: |
|f.text(*s*, *x*, *y*[, *c*])|Write text to the FrameBuffer using the the coordinates as the upper-left corner of the text. The color of the text can be defined by the optional argument but is otherwise a default value of 1. All characters have dimensions of 8x8 pixels and there is currently no way to change the font.|
##
## **Other methods**
|<p>FrameBuffer function (f)</p><p>eg display.fill(c)</p>|Description|
| :-: | :-: |
|f.scroll(*xstep*, *ystep*)|Shift the contents of the FrameBuffer by the given vector. This may leave a footprint of the previous colors in the FrameBuffer.|
|f.blit(*fbuf*, *x*, *y*, *key=-1*, *palette=None*)|<p>Draw another FrameBuffer on top of the current one at the given coordinates. If *key* is specified then it should be a color integer and the corresponding color will be considered transparent: all pixels with that color value will not be drawn. (If the *palette* is specified then the *key* is compared to the value from *palette*, not to the value directly from *fbuf*.)</p><p>The *palette* argument enables blitting between FrameBuffers with differing formats. Typical usage is to render a monochrome or grayscale glyph/icon to a color display. The *palette* is a FrameBuffer instance whose format is that of the current FrameBuffer. The *palette* height is one pixel and its pixel width is the number of colors in the source FrameBuffer. The *palette* for an N-bit source needs 2\*\*N pixels; the *palette* for a monochrome source would have 2 pixels representing background and foreground colors. The application assigns a color to each pixel in the *palette*. The color of the current pixel will be that of that *palette* pixel whose x position is the color of the corresponding source pixel.</p>|

## **Constants**
|<p>FrameBuffer function (f)</p><p>eg display.fill(c)</p>|Description|
| :-: | :-: |
|f.MONO\_VLSB|Monochrome (1-bit) color format This defines a mapping where the bits in a byte are vertically mapped with bit 0 being nearest the top of the screen. Consequently each byte occupies 8 vertical pixels. Subsequent bytes appear at successive horizontal locations until the rightmost edge is reached. Further bytes are rendered at locations starting at the leftmost edge, 8 pixels lower.|
|f.MONO\_HLSB|Monochrome (1-bit) color format This defines a mapping where the bits in a byte are horizontally mapped. Each byte occupies 8 horizontal pixels with bit 7 being the leftmost. Subsequent bytes appear at successive horizontal locations until the rightmost edge is reached. Further bytes are rendered on the next row, one pixel lower.|
|f.MONO\_HMSB|Monochrome (1-bit) color format This defines a mapping where the bits in a byte are horizontally mapped. Each byte occupies 8 horizontal pixels with bit 0 being the leftmost. Subsequent bytes appear at successive horizontal locations until the rightmost edge is reached. Further bytes are rendered on the next row, one pixel lower.|
|f.RGB565|Red Green Blue (16-bit, 5+6+5) color format|
|f.GS2\_HMSB|Grayscale (2-bit) color format|
|f.GS4\_HMSB|Grayscale (4-bit) color format|
|f..GS8|Grayscale (8-bit) color format|


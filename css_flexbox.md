# CSS Flexbox

> Brief summary of _CSS Flexbox_ part of _Responsive Web Design Certification_ course on [freeCodeCamp](https://learn.freecodecamp.org/).

---
Placing the CSS property `display: flex;` on an element allows you to use other flex properties to build a responsive page.
```css
header {
    display: flex;
}
```
This makes it possible to align any children of that element into rows or columns. You do this by adding the `flex-direction` property to the parent item and setting it to:
 - `row`; 
 - `column`;
 - `row-reverse`;
 - `column-reverse`;
 The default value for the flex-direction property is `row`.

```css
#box-container {
    display: flex;
    flex-direction: row-reverse;
}
```

---
`justify-content` property has several options to tell CSS how to align and space out the flex items a certain way. Recall that setting a flex container as a row places the flex items side-by-side from left-to-right. A flex container set as a column places the flex items in a vertical stack from top-to-bottom. For each, the direction the flex items are arranged is called the main axis. For a row, this is a horizontal line that cuts through each item. And for a column, the main axis is a vertical line through the items.

There are several options for how to space the flex items along the line that is the main axis.
 - `justify-content: center;` - which aligns all the flex items to the center inside the flex container.
 - `flex-start`; - aligns items to the start of the flex container. For a row, this pushes the items to the left of the container. For a column, this pushes the items to the top of the container.
 - `flex-end`; - aligns items to the end of the flex container. For a row, this pushes the items to the right of the container. For a column, this pushes the items to the bottom of the container.
 - `space-between`; - aligns items to the center of the main axis, with extra space placed between the items. The first and last items are pushed to the very edge of the flex container.
 - `space-around`; - similar to space-between but the first and last items are not locked to the edges of the container, the space is distributed around all the items

```css
 #box-container {
    display: flex;
    flex-direction: center;
}
```

---
The `align-items` property is similar to `justify-content`. CSS offers the align-items property to align flex items along the cross axis. For a row, it tells CSS how to push the items in the entire row up or down within the container. And for a column, how to push all the items left or right within the container.

The different values available for `align-items` include:
 - `flex-start`; - aligns items to the start of the flex container. For rows, this aligns items to the top of the container. For columns, this aligns items to the left of the container.
 - `flex-end`; - aligns items to the end of the flex container.
 - `center`; - align items to the center.
 - `stretch`; - stretch the items to fill the flex container. For example, rows items are stretched to fill the flex container top-to-bottom.
 - `baseline`: align items to their baselines. Baseline is a text concept, think of it as the line that the letters sit on.

```css
#box-container {
    align-items: stretch;
}
```

---
CSS flexbox has a feature to split a flex item into multiple rows (or columns). By default, a flex container will fit all flex items together. For example, a row will all be on one line. However, using the `flex-wrap` property, it tells CSS to wrap items. This means extra items move into a new row or column. The break point of where the wrapping happens depends on the size of the items and the size of the container.

CSS also has options for the direction of the wrap:
 - `nowrap`; - this is the default setting, and does not wrap items.
 - `wrap`; - wraps items from left-to-right if they are in a row, or top-to-bottom if they are in a column.
 - `wrap-reverse`; - wraps items from bottom-to-top if they are in a row, or right-to-left if they are in a column.

```css
#box-container {
    flex-wrap: wrap-reverse;
}
```

---
You can use `align-content` to set how multiple lines are spaced apart from each other. This property takes the following values:
 - `flex-start`: Lines are packed at the top of the container.
 - `flex-end`: Lines are packed at the bottom of the container.
 - `center`: Lines are packed at the vertical center of the container.
 - `space-between`: Lines display with equal spacing between them.
 - `space-around`: Lines display with equal spacing around them.
 - `stretch`: Lines are stretched to fit the container.

This can be confusing, but `align-content` determines the spacing between lines, while `align-items` determines how the items as a whole are aligned within the container. When there is only one line, `align-content` has no effect.

```css
#box-container {
    flex-wrap: wrap-reverse;
    align-content: center;
}
```

---
The two properties `flex-direction` and `flex-wrap` are used so often together that the shorthand property `flex-flow` was created to combine them. This shorthand property accepts the value of one of the two properties separated by a space.

```css
#box-container {
    flex-flow: row wrap;
}
```

---
So far, all the properties apply to the flex container (the parent of the flex items). However, there are several useful properties for the flex items. 

`flex-shrink` property allows an item to shrink if the flex container is too small. Items shrink when the width of the parent container is smaller than the combined widths of all the flex items within it.

The `flex-shrink` property takes numbers as values. The higher the number, the more it will shrink compared to the other items in the container. For example, if one item has a `flex-shrink` value of 1 and the other has a `flex-shrink` value of 3, the one with the value of 3 will shrink three times as much as the other.

```css
#box-1 {
    flex-shrink: 2;
}

#box-2 {
    flex-shrink: 1;
}
```

---
The opposite of `flex-shrink` is the `flex-grow` property. It controls the size of items when the parent container expands. If one item has a `flex-grow` value of 1 and the other has a `flex-grow` value of 3, the one with the value of 3 will grow three times as much as the other.

```css
#box-1 {
    flex-grow: 3;
}

#box-2 {
    flex-grow: 2;
}
```

---
The `flex-basis` property specifies the initial size of the item before CSS makes adjustments with flex-shrink or flex-grow. The units used by the `flex-basis` property are the same as other size properties (px, em, %, etc.). The value auto sizes items based on the content.

```css
#box-1 {
    flex-basis: 10em;
}

#box-2 {
    flex-basis: 20em;
}
```

The `flex-grow`, `flex-shrink`, and `flex-basis` properties can all be set together by using the flex property. The default property settings are `flex: 0 1 auto;`. This will set the item to `flex-grow: 1;`, `flex-shrink: 0;`, and `flex-basis: 10px;`

```css
#box-2 {
    flex: 1 0 10px;
}
```

---
The `order` property is used to tell CSS the order of how flex items appear in the flex container. By default, items will appear in the same order they come in the source HTML. The property takes numbers as values, and negative numbers can be used.

```css
#box-1 {
    order: 1;
}

#box-2 {
    order: -1;
}
```

---
`align-self` property allows you to adjust each item's alignment individually, instead of setting them all at once. This is useful since other common adjustment techniques using the CSS properties `float`, `clear`, and `vertical-align` do not work on flex items. `align-self` accepts the same values as `align-items` and will override any value set by the `align-items` property.

```css
#box-1 {
    align-self: center;
}

#box-2 {
    align-self: flex-end;
}
```

---

# Additional resources

 - [A Complete Guide to Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
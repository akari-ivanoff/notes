# CSS Grid

> Brief summary of _CSS Grid_ part of _Responsive Web Design Certification_ course on [freeCodeCamp](https://learn.freecodecamp.org/).

---
Turn any HTML element into a grid container by setting its `display` property to `grid`. This gives you the ability to use all the other properties associated with CSS Grid. In CSS Grid, the parent element is referred to as the container and its children are called items.

```css
.container {
    display: grid;
}
```

---
To add some columns to the grid, use the `grid-template-columns` property on a grid container. This will give your grid two columns that are 50px wide each. The number of parameters given to the `grid-template-columns` property indicates the number of columns in the grid, and the value of each parameter indicates the width of each column.


```css
.container {
    display: grid;
    grid-template-columns: 50px 50px;
}
```

---
The grid will set the number of rows automatically. To adjust the rows manually, use the `grid-template-rows` property.

```css
.container {
    display: grid;
    grid-template-rows: 50px 50px;
}
```

----
You can use absolute and relative units like _px_ and _em_ in CSS Grid to define the size of rows and columns. You can use these as well:
 - _fr_: sets the column or row to a fraction of the available space,
 - _auto_: sets the column or row to the width or height of its content automatically,
 - _%_: adjusts the column or row to the percent width of its container.

This snippet creates five columns. The first column is as wide as its content, the second column is 50px, the third column is 10% of its container, and for the last two columns; the remaining space is divided into three sections, two are allocated for the fourth column, and one for the fifth.

```css
.container {
    display: grid;
    grid-template-columns: auto 50px 10% 2fr 1fr;
}
```

---
To add a gap between the columns, use the `grid-column-gap` property. This creates 10px of empty space between all of our columns:

```css
.container {
    grid-column-gap: 10px;
}
```

---
You can add a gap in between the rows of a grid using `grid-row-gap`:

```css
.container {
    grid-row-gap: 10px;
}
```

---
`grid-gap` is a shorthand property for `grid-row-gap` and `grid-column-gap`. If `grid-gap` has one value, it will create a gap between all rows and columns. However, if there are two values, it will use the first one to set the gap between the rows and the second value for the columns.

```css
.container {
    grid-gap: 10px 20px;
}
```

---
The hypothetical horizontal and vertical lines that create the grid are referred to as lines. These lines are numbered starting with 1 at the top left corner of the grid and move right for columns and down for rows, counting upward.

To control the amount of columns an item will consume, you can use the `grid-column` property in conjunction with the line numbers you want the item to start and stop at.

The following example will make the item start at the first vertical line of the grid on the left and span to the 3rd line of the grid, consuming two columns.

```css
.item5 {
    grid-column: 1 / 3;
}
```

---
You can make items consume multiple rows just like you can with columns. You define the horizontal lines you want an item to start and stop at using the `grid-row` property on a grid item.

```css
.item5 {
    grid-row: 2 / 4;
}
```

---
In CSS Grid, the content of each item is located in a box which is referred to as a cell. You can align the content's position within its cell horizontally using the `justify-self` property on a grid item. By default, this property has a value of `stretch`, which will make the content fill the whole width of the cell. This CSS Grid property accepts other values as well:
 - `start` - aligns the content at the left of the cell,
 - `center`  - aligns the content in the center of the cell,
 - `end` - aligns the content at the right of the cell.

```css 
.item2 {
    justify-self: center;
}
```

---
Just as you can align an item horizontally, there's a way to align an item vertically as well. To do this, you use the `align-self` property on an item. This property accepts all of the same values as `justify-self`.

```css
.item3 {
    align-self: end;
}
```

---
Sometimes you want all the items in your CSS Grid to share the same alignment. You can use the previously learned properties and align them individually, or you can align them all at once horizontally by using `justify-items` on your grid container. This property can accept all the same values you learned about, the difference being that it will move all the items in our grid to the desired alignment.

```css
.container {
    justify-items: center; 
}
```

---
Using the `align-items`: property on a grid container will set the vertical alignment for all the items in our grid.

```css
.container {
    align-items: center; 
}
```

---
You can group cells of your grid together into an area and give the area a custom name. Do this by using `grid-template-areas` on the container. The code below merges the top three cells together into an area named header, the bottom three cells into a footer area, and it makes two areas in the middle row; advert and content. Every word in the code represents a cell and every pair of quotation marks represent a row. In addition to custom labels, you can use a period (`.`) to designate an empty cell in the grid.

```css
.container {
    grid-template-areas:
        "header header header"
        "advert content content"
        "footer footer footer";
}
```

---
After creating an areas template for your grid container, you can place an item in your custom area by referencing the name you gave it. To do this, you use the `grid-area` property on an item. The following example lets the grid know that you want the item1 class to go in the area named header. In this case, the item will use the entire top row because that whole row is named as the header area.

```css
.item1 {
    grid-area: header;
}
```

---
The `grid-area` property can be used in another way. If your grid doesn't have an areas template to reference, you can create an area on the fly for an item to be placed. This is using the line numbers to define where the area for this item will be. The numbers in the example represent these values:

`grid-area: horizontal line to start at / vertical line to start at / horizontal line to end at / vertical line to end at;`

So the item in the example will consume the rows between lines 1 and 2, and the columns between lines 1 and 4.

```css
item1 {
    grid-area: 1/1/2/4;
}
```

---
When you used `grid-template-columns` and `grid-template-rows` to define the structure of a grid, you entered a value for each row or column you created. Lets say you want a grid with 100 rows of the same height. It isn't very practical to insert 100 values individually. Fortunately, there's a better way - by using the `repeat` function to specify the number of times you want your column or row to be repeated, followed by a comma and the value you want to repeat. Here's an example that would create the 100 row grid, each row at 50px tall.

```css
.container {
    grid-template-rows: repeat(100, 50px);
}
```

---
There's another built-in function to use with `grid-template-columns` and `grid-template-rows` called `minmax`. It's used to limit the size of items when the grid container changes size. To do this you need to specify the acceptable size range for your item.

In the code below, `grid-template-columns` is set to create two columns; the first is _100px_ wide, and the second has the minimum width of _50px_ and the maximum width of _200px_.

```css
.container {
    grid-template-columns: 100px minmax(50px, 200px);
}
```

---
The `repeat` function comes with an option called `auto-fill`. This allows you to automatically insert as many rows or columns of your desired size as possible depending on the size of the container. You can create flexible layouts when combining `auto-fill` with `minmax`.

In the example, when the container changes size, this setup keeps inserting _60px_ columns and stretching them until it can insert another one.

Note: if your container can't fit all your items on one row, it will move them down to a new one.

```css
.container {
    repeat(auto-fill, minmax(60px, 1fr));
}
```

---
`auto-fit` works almost identically to `auto-fill`. The only difference is that when the container's size exceeds the size of all the items combined, `auto-fill` keeps inserting empty rows or columns and pushes your items to the side, while `auto-fit` collapses those empty rows or columns and stretches your items to fit the size of the container.

Note: if your container can't fit all your items on one row, it will move them down to a new one.

```css
.container {
    repeat(auto-fit, minmax(60px, 1fr));
}
```

---
CSS Grid can be an easy way to make your site more responsive by using media queries to rearrange grid areas, change dimensions of a grid, and rearrange the placement of items.

In the example, when the viewport width is 300px or more, the number of columns changes from 1 to 2. The advertisement area then occupies the left column completely.

```css
.container {
    grid-template-areas:
        "header"
        "advert"
        "content"
        "footer";
}
  
@media (min-width: 300px){
    .container{
        grid-template-areas:
            "advert header"
            "advert content"
            "advert footer";
    }
}
```

---
Turning an element into a grid only affects the behavior of its direct descendants. So by turning a direct descendant into a grid, you have a grid within a grid.

For example, by setting the `display` and `grid-template-columns` properties of the element with the _item3_ class, you create a grid within your grid.

```html
<style>
.container {
    display: grid;
}
.item3 {
    display: grid;
    grid-template-columns: auto 1fr;
}
</style>

<div class="container">
  <div class="item3">
    <div class="itemOne">paragraph1</div>
    <div class="itemTwo">paragraph2</div>
  </div>
</div>
```

---
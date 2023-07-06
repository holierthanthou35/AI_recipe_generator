function
addToShoppingList(item)
{
    const
shoppingList = document.getElementById('shopping-list');
const
listItem = document.createElement('li');
listItem.textContent = item;
shoppingList.appendChild(listItem);
}



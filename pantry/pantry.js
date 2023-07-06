const pantryBtns = document.querySelectorAll(".pantry-btn");
const shoppingList = document.getElementById("shopping-list");

pantryBtns.forEach(btn => {
	btn.addEventListener("click", async () => {
		const listItem = document.createElement("li");
		const itemContent = btn.dataset.content;
		const itemContentArray = itemContent.split(" ");

		for (var i = 0; i < itemContentArray.length; i++) {
			itemContentArray[i] =
				itemContentArray[i].charAt(0).toUpperCase() +
				itemContentArray[i].slice(1);
		}

		const newItemContent = itemContentArray.join(" ");

		listItem.textContent = newItemContent;
		shoppingList.appendChild(listItem);

		const rawResponse = await fetch("http://localhost:5000/item", {
			method: "POST",
			headers: {
				Accept: "application/json",
				"Content-Type": "application/json",
			},
			body: JSON.stringify({ item: newItemContent }),
		});
		const content = await rawResponse.json();
	});
});

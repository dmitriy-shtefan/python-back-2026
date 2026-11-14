(() => {
  const searchPanel = document.querySelector("#search-panel");
  if (!searchPanel) return;

  const search = document.querySelector("#search");
  const searchStatus = document.querySelector("#search-status");
  const cards = document.querySelectorAll(".cards li");

  search.addEventListener("input", () => {
    const query = search.value.trim().toLowerCase();
    let matches = 0;

    for (const card of cards) {
      card.hidden = !card.dataset.search.toLowerCase().includes(query);
      if (!card.hidden) matches += 1;
    }

    searchStatus.textContent = matches ? `Збігів: ${matches}` : "Нічого не знайдено.";
  });

  searchPanel.hidden = false;
})();

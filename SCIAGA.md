# 🎯 Ściąga na obronę — Katalog Albumów (React)

> Prawie wszystko, o co pyta prowadzący, jest w **jednym pliku: `src/App.jsx`**.
> Polskie znaki = `index.html` + `localeCompare`. Tyle musisz wiedzieć na start.

---

## 🗺️ Mapa: gdzie co jest

| Temat | Plik | Czego szukać |
|---|---|---|
| Sortowanie | `App.jsx` | `switch (filters.sortBy)` |
| Filtrowanie | `App.jsx` | linijki z `.filter(...)` (nad sortowaniem) |
| CRUD | `App.jsx` | funkcje `addAlbum`, `deleteAlbum`, `updateAlbum`, `toggleStatus` |
| Polskie znaki | `index.html` + `App.jsx` | `charset="UTF-8"` + `localeCompare` |
| Walidacja | `AlbumForm.jsx` | funkcja `validate` |
| `key` na liście | `AlbumList.jsx` | `key={album.id}` |
| localStorage | `hooks/useLocalStorage.js` | własny hook |

---

## 1️⃣ STAN — gdzie mieszkają dane

```js
const [albums, setAlbums] = useLocalStorage('albums', initialAlbums)
const [filters, setFilters] = useLocalStorage('filters', {
  search: '', genre: '', status: '', sortBy: 'title-asc',
})
const [editingAlbum, setEditingAlbum] = useState(null)
const [showForm, setShowForm] = useState(false)
```

**Prosto:** cały stan aplikacji siedzi tu, w `App`. `albums` = kolekcja, `filters` = ustawienia szukania/sortowania (oba zapisują się do localStorage). `editingAlbum` = który album edytuję, `showForm` = czy pokazać formularz.

🗣️ **Co mówić:** „Cały stan trzymam tutaj, w App. Albumy i filtry lecą do localStorage, dwa pozostałe sterują formularzem."

---

## 2️⃣ SORTOWANIE

```js
filteredAlbums = [...filteredAlbums].sort((a, b) => {
  switch (filters.sortBy) {
    case 'title-asc':   return a.title.localeCompare(b.title)
    case 'title-desc':  return b.title.localeCompare(a.title)
    case 'year-newest': return b.year - a.year
    case 'year-oldest': return a.year - b.year
    case 'rating-high': return b.rating - a.rating
    default: return 0
  }
})
```

**Prosto:** user wybiera z menu (tytuł / rok / ocena), a ja sortuję listę. Tekst sortuję przez `localeCompare`, liczby przez odejmowanie (`b - a` = malejąco, `a - b` = rosnąco).

🗣️ **Co mówić:** „Tu sortuję — zależnie od wyboru, po tytule, roku albo ocenie. Tekst przez `localeCompare`, **żeby polskie znaki szły alfabetycznie**, liczby przez odejmowanie. Sortuję **po** filtrowaniu."

🔑 **Słowo-klucz:** `localeCompare` = polskie znaki w sortowaniu.

---

## 3️⃣ FILTROWANIE

```js
let filteredAlbums = albums.filter((a) => {
  const q = filters.search.toLowerCase()
  return a.title.toLowerCase().includes(q) ||
         a.artist.toLowerCase().includes(q)
})

if (filters.genre)  filteredAlbums = filteredAlbums.filter((a) => a.genre === filters.genre)
if (filters.status) filteredAlbums = filteredAlbums.filter((a) => a.status === filters.status)
```

**Prosto:** trzy filtry jeden po drugim. Najpierw wyszukiwarka (po tytule LUB artyście), potem gatunek, potem status. `toLowerCase` po obu stronach = wielkość liter nie ma znaczenia.

🗣️ **Co mówić:** „Filtruję w trzech krokach: wyszukiwarka po tytule i artyście, potem gatunek i status. Filtry się łączą. Na końcu idzie sortowanie."

🔑 **Słowo-klucz:** najpierw filtr → potem sort. `toLowerCase` = nieważna wielkość liter.

---

## 4️⃣ CRUD (dodaj / usuń / edytuj / status)

**Wspólna zasada:** nigdy nie zmieniam tablicy w miejscu — zawsze robię nową. Dlatego React odświeża widok.

### ➕ Dodawanie
```js
const addAlbum = (albumData) => {
  const newAlbum = { ...albumData, id: Date.now() }
  setAlbums((prev) => [...prev, newAlbum])
  setShowForm(false)
}
```
🗣️ „Biorę dane z formularza, doklejam unikalne `id` z `Date.now()` i dodaję album do tablicy."

### 🗑️ Usuwanie
```js
const deleteAlbum = (id) => {
  if (window.confirm('Czy na pewno chcesz usunac ten album?')) {
    setAlbums((prev) => prev.filter((a) => a.id !== id))
  }
}
```
🗣️ „Najpierw `confirm` jako potwierdzenie, potem `filter` zostawia wszystkie **oprócz** tego id."
🔑 confirm = potwierdzenie usunięcia (punkt z polecenia).

### ✏️ Edycja
```js
const updateAlbum = (updatedAlbum) => {
  setAlbums((prev) =>
    prev.map((a) => (a.id === updatedAlbum.id ? updatedAlbum : a))
  )
}
```
🗣️ „`map` przechodzi po wszystkich i podmienia tylko ten o pasującym id, reszta bez zmian."

### 🔁 Zmiana statusu
```js
const toggleStatus = (id) => {
  const cycle = { owned: 'listening', listening: 'wishlist', wishlist: 'owned' }
  setAlbums((prev) => prev.map((a) =>
    a.id === id ? { ...a, status: cycle[a.status || 'owned'] } : a
  ))
}
```
🗣️ „Status zmienia się w kółko: posiadane → słucham → lista życzeń → z powrotem."

---

## 5️⃣ POLSKIE ZNAKI

**Dwa miejsca:**

```html
<!-- index.html -->
<meta charset="UTF-8" />
```
```js
// App.jsx — sortowanie
a.title.localeCompare(b.title)
```

🗣️ **Co mówić:** „Polskie znaki działają, bo mam UTF-8 w `index.html`, a w sortowaniu używam `localeCompare`, który poprawnie układa ą, ć, ł alfabetycznie."

---

## 6️⃣ CO SIĘ WYŚWIETLA (JSX na dole App)

```jsx
<Statistics albums={albums} />
<SearchFilter filters={filters} onFiltersChange={setFilters} />
<button onClick={openAddForm}>+ Dodaj album</button>

{showForm && ( <modal> <AlbumForm .../> </modal> )}

<AlbumList albums={filteredAlbums} onDelete={...} onEdit={...} onToggleStatus={...} />
```

**Prosto:** statystyki, filtry, przycisk dodawania, niżej lista. Formularz pokazuje się **tylko gdy `showForm` jest true** (`{showForm && ...}`). Do listy idą **przefiltrowane** albumy, nie wszystkie.

🗣️ **Co mówić:** „Tu układam widok. Formularz w okienku pojawia się tylko gdy `showForm` jest true. Do listy przekazuję przefiltrowaną tablicę."

---

# ❓ DODATKOWE PYTANIA — rozpisane na spokojnie

### „Dlaczego stan trzymasz w App, a nie w komponentach?"
Bo kilka komponentów korzysta z tych samych danych (lista, statystyki, filtry). Gdyby każdy miał własną kopię, nie byłyby zgrane. Trzymam dane **w jednym miejscu wyżej**, a komponenty dostają je przez `props`.

🗣️ „Trzymam stan w App, bo kilka komponentów go używa. Dzięki temu wszystkie patrzą na te same dane."

---

### „Po co przekazujesz funkcje do komponentów (onDelete, onEdit)?"
Komponent dziecka (np. karta albumu) **nie zmienia danych sam**. Gdy klikniesz „Usuń", on tylko **woła moją funkcję** `onDelete(id)`, a prawdziwe usunięcie dzieje się w App.

```jsx
// w App przekazuję funkcję w dół:
<AlbumList onDelete={deleteAlbum} ... />
// dziecko ją tylko wywołuje, gdy klikniesz przycisk:
<button onClick={() => onDelete(id)}>Usuń</button>
```

🗣️ „Dane mieszkają w App, więc dziecko nie usuwa samo — woła moją funkcję, a ja zmieniam stan u siebie." (To się nazywa **przekazywanie danych w górę**.)

---

### „Czemu `[...prev, newAlbum]` zamiast `push`?"
W Reakcie **nie wolno zmieniać stanu bezpośrednio**. `albums.push(...)` zmieniłby starą tablicę i React **by nie zauważył** zmiany — widok by się nie odświeżył. Dlatego robię **nową** tablicę (`[...prev, x]`), wtedy React widzi „o, nowe dane" i przerysowuje.

🗣️ „Bo w Reakcie tworzy się nowy stan zamiast zmieniać stary — inaczej widok się nie odświeży."

---

### „Gdzie jest `key` i czemu akurat tam?"
W `AlbumList.jsx`, przy renderowaniu listy:
```jsx
{albums.map((album) => (
  <AlbumCard key={album.id} album={album} ... />
))}
```
`key` to unikalny znacznik każdego elementu listy — React po nim wie, co się zmieniło. Daję **`id`, nie numer w kolejności (indeks)**, bo po usunięciu elementu indeksy się przesuwają i React mógłby pomieszać karty.

🗣️ „`key` jest w AlbumList przy `.map()`. Daję id, nie indeks, żeby przy usuwaniu nic się nie pomieszało."

---

### „Gdzie walidacja formularza?"
W `AlbumForm.jsx`, funkcja `validate`:
```js
const validate = () => {
  const newErrors = {}
  if (!formData.title || formData.title.trim().length < 2)
    newErrors.title = 'Tytuł jest wymagany (min. 2 znaki)'
  // ...sprawdzenie artysty, roku, oceny
  return newErrors
}
```
Sprawdza pola, zbiera błędy. Jak są błędy — **blokuje wysłanie** i pokazuje czerwone komunikaty przy polach.

🗣️ „Walidacja jest w AlbumForm, funkcja `validate`. Sprawdza pola, a jak coś źle, pokazuje błąd i nie pozwala wysłać."

---

### „Skąd dane po odświeżeniu strony?"
Z **localStorage**, przez mój własny hook `useLocalStorage.js`. Działa jak zwykły `useState`, ale dodatkowo zapisuje wszystko w przeglądarce, więc dane przeżywają odświeżenie.

🗣️ „Z localStorage. Mam własny hook `useLocalStorage`, który zapisuje albumy i filtry, żeby nie znikały po odświeżeniu."

---

### „Jeden formularz dodaje i edytuje — jak?"
Po `editingAlbum`:
- `editingAlbum = null` → formularz pusty → **dodawanie**
- `editingAlbum = album` → formularz wypełniony danymi → **edycja**

```jsx
<AlbumForm
  album={editingAlbum}
  onSubmit={editingAlbum ? updateAlbum : addAlbum}
/>
```

🗣️ „Ten sam formularz robi obie rzeczy. Jak `editingAlbum` jest pusty — dodaję, jak ma album — edytuję."

---

### „Gdzie useState i useEffect?" (czasem o to pytają wprost)
- **useState** — w `App` (formularz), w `AlbumForm`, a w hooku pod spodem.
- **useEffect** — w `App` (log przy zmianie albumów) i w `AlbumForm` (przeładowanie pól przy edycji innego albumu).

🗣️ „useState mam w App i formularzu, useEffect w App przy zmianie albumów i w formularzu przy edycji."

---

## 🧠 Jedno zdanie na całość
> „Cały stan i logika — CRUD, filtrowanie, sortowanie — są w `App.jsx`. Komponenty obok tylko wyświetlają: lista, formularz, statystyki, filtry. Dane lecą do localStorage przez mój własny hook. Polskie znaki ogarnia UTF-8 i `localeCompare`."

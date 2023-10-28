async function handleFilterChange() {
    const selectedValue = document.getElementById('filterDropdown').value;
    refreshProducts(selectedValue);
}

function punten(type, message) {
    const modal = document.getElementById('myModal');
    modal.textContent = message;
    modal.className = type;
    modal.style.display = 'block';

    setTimeout(function() {
        modal.style.display = 'none';
    }, 3000);  // Hide the modal after 3 seconds
}

async function updateJumlahItem() {
try {
    const response = await fetch("get_jumlah_item/");
    if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const data = await response.json();
    const jumlahItemElement = document.getElementById("jumlah_item");

    if (jumlahItemElement) {
        jumlahItemElement.textContent = data.jumlah_item;
    }
} catch (error) {
    console.error('Error updating jumlah item:', error);
}
}
// Panggil fungsi updateJumlahItem saat halaman dimuat
updateJumlahItem();
refreshProducts("all");
async function getProducts(filter) {
    const url = `get-product/${filter}`;
    const response = await fetch(url);

    if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
    }

    return response.json();
}


async function deleteProduct(item_id) {
try {
    const csrftoken = getCsrfToken();
    const response = await fetch(`delete_item/${item_id}/`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
    });

    if (!response.ok) {
        throw new Error('Gagal menghapus produk.');
    }

    const data = await response.json();
    updateJumlahItem();
    console.log(data.message);
    // Logika atau pembaruan tampilan sesuai kebutuhan
} catch (error) {
    console.error('Terjadi kesalahan:', error);
}
}

// Fungsi untuk mendapatkan nilai csrftoken
function getCsrfToken() {
// Gantilah dengan cara mendapatkan csrftoken sesuai dengan proyek atau framework yang kamu gunakan
// Misalnya, jika menggunakan Django, bisa menggunakan document.querySelector('[name=csrfmiddlewaretoken]').value
return document.querySelector('[name=csrfmiddlewaretoken]').value;
}


async function refreshProducts(filter) {
console.log('daadad');
updateJumlahItem();
document.getElementById("product_table").innerHTML = "";
const products = await getProducts(filter);
console.log(products);
let htmlString = '<div class="d-flex flex-row flex-wrap">';  // Flex container

products.forEach((item, index) => {
    const cardClass = index === products.length - 1 ? '' : '';  // Add bg-warning class for the last card
    htmlString += `
        <div class="card m-3 ${cardClass}" style="width: 18rem;">
            <div class="card-body">
                <h5 class="card-title">Judul: ${item.fields.judul_buku}</h5>
                <p class="card-text">Petugas: ${item.fields.petugas}</p>
                <p class="card-text">Durasi: ${item.fields.durasi_pinjam} hari</p>
                <p class="card-text">Description: ${item.fields.catatan_peminjaman}</p>
                <p class="card-text">User id: ${item.fields.user}</p>
                <div class="row">
                    <div class="col">
                        <button class="delete-button" data-item-id="${item.pk}">Kembalikan</button>
                    </div>
                </div>
            </div>
        </div>`;
});

htmlString += '</div>';  // Close flex container
document.getElementById("product_table").innerHTML = htmlString;

document.getElementById("product_table").innerHTML = htmlString;

// Menambahkan event listener untuk setiap tombol hapus
document.querySelectorAll('.delete-button').forEach((button) => {
button.addEventListener('click', async () => {
    const itemId = button.getAttribute('data-item-id');
    console.log('Button clicked. Item ID:', itemId);
    await deleteProduct(itemId);
    handleFilterChange(); // Refresh tabel setelah menghapus item
});
});

}

async function addProduct() {
    const response = await fetch("create-product-ajax/", {
        method: "POST",
        body: new FormData(document.querySelector('#form'))
    });

    const data = await response.json();

    if (data.status === 'error') {
        // Tampilkan modal untuk buku tidak ditemukan
        punten('error','Buku tidak ditemukan');
        document.getElementById("form").reset()
    } else {
        // Buku ditemukan, lanjutkan dengan tindakan lainnya
        refreshProducts("all");
        handleFilterChange();
        document.getElementById("form").reset();
    }
    return false;
}

document.getElementById("button_add").onclick = addProduct;


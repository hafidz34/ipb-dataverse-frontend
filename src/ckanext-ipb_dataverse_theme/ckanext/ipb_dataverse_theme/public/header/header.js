function toggleDropdown(event) {
    event.stopPropagation();
    var btn = event.currentTarget;
    
    // Cari elemen menu yang merupakan sibling dari button
    // Dalam struktur HTML kita, div.ipb-menu-box ada tepat setelah button
    var wrapper = btn.parentElement;
    var menu = wrapper.querySelector('.ipb-menu-box');
    var icon = btn.querySelector('.fa-chevron-down');

    // Tutup menu lain jika ada yang terbuka
    document.querySelectorAll('.ipb-menu-box').forEach(function(el) {
        if (el !== menu) el.classList.remove('show');
    });

    // Toggle menu yang diklik
    menu.classList.toggle('show');
    
    // Putar ikon panah
    if(icon) {
        if (menu.classList.contains('show')) {
            icon.style.transform = 'rotate(180deg)';
        } else {
            icon.style.transform = 'rotate(0deg)';
        }
        icon.style.transition = '0.2s';
    }
}

// Tutup menu jika klik di luar area
window.addEventListener('click', function(e) {
    document.querySelectorAll('.ipb-menu-box.show').forEach(function(menu) {
        // Jika yang diklik bukan menu dan bukan bagian dari parent (tombol)
        if (!menu.parentElement.contains(e.target)) {
            menu.classList.remove('show');
            
            // Reset ikon panah
            var wrapper = menu.parentElement;
            var icon = wrapper.querySelector('.fa-chevron-down');
            if(icon) icon.style.transform = 'rotate(0deg)';
        }
    });
});
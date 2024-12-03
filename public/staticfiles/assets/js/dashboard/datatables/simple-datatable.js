window.addEventListener('DOMContentLoaded', event => {
    const tableIds = ['offers_table', 'assets_table'];
    tableIds.forEach(id => {
        const table = document.getElementById(id);
        if (table) {
            new simpleDatatables.DataTable(table);
        }
    });
});
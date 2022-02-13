export default [
    {
        name: 'id',
        required: true,
        label: 'ID',
        align: 'center',
        field: row => row.id,
        // format: val => `${val}`,
        sortable: true
    },
    {
        name: 'avatar',
        required: true,
        label: 'Nombre',
        align: 'center',
    },
    {
        name: 'name',
        required: true,
        label: 'Nombre',
        align: 'center',
        field: row => row.name,
        // format: val => `${val}`,
        sortable: true
    },
    {
        name: 'last_name',
        required: true,
        label: 'Apellidos',
        align: 'center',
        field: row => row.last_name,
        // format: val => `${val}`,
        sortable: true
    },
    {
        name: 'area',
        required: true,
        label: 'Tipo de Area',
        align: 'center',
        field: row => row.area_type.name,
        // format: val => `${val}`,
        sortable: true
    },
    {
        name: 'status',
        required: true,
        label: 'Estado',
        align: 'center',
        field: row => row.status,
        // format: val => `${val}`,
        sortable: true
    },
    {
        name: 'actions',
        required: true,
        label: '',
        align: 'center',
        field: row => row.city,
        // format: val => `${val}`,
        sortable: true
    }
]
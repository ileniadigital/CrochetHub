<template>
    <!-- Add modal -->
    <Add :model="model" :data="computedData" :fields="fields" @added="fetchData" @update="updateData" />

    <!-- Headings -->
    <div class="container text-center">
        <div class="row">
            <div class="col" v-for="(header, index) in headers" :key="index">
                {{ header }}
            </div>
            <div class="col"></div>
        </div>
    </div>

    <!-- Render data -->
    <ul class="list-group">
        <li class="list-group-item" v-for="(item, index) in items" :key="item.id || index">
            <div class="info">
                <div v-for="field in fields" :key="field" class="data-field item">
                    <template v-if="field === 'link'">
                        <a :href="item[field]">View</a>
                    </template>
                    <template v-else>
                        {{ item[field] }}
                    </template>
                </div>
                <div class="buttons">
                    <button @click="openEditModal(item)" class="btn btn-primary" type="button">
                        <i class="bi bi-pencil-square">Edit</i>
                    </button>
                    <button @click="openDeleteModal(item.id)" class="btn btn-danger" type="button">
                        <i class="bi bi-trash">Delete</i>
                    </button>
                </div>
            </div>
        </li>
    </ul>

    <!-- Conditionally render the Edit component -->
    <Edit ref="editModal" v-if="activeItem" :model="model" :data="activeItem" @edited="fetchData"
        @close="closeEditModal" />

    <!-- Conditionally render the Delete component -->
    <Delete ref="deleteModal" v-if="activeDeleteId" :model="model" :id="activeDeleteId" @deleted="fetchData"
        @close="closeDeleteModal" />
</template>

<script>
import Add from '../Action/Add.vue';
import Edit from '../Action/Edit.vue';
import Delete from '../Action/Delete.vue';
import * as bootstrap from 'bootstrap';
import { nextTick } from 'vue';

export default {
    components: {
        Add,
        Edit,
        Delete
    },
    props: {
        model: {
            type: String,
            required: true
        },
        fields: {
            type: Array,
            required: true
        },
        headers: {
            type: Array,
            required: true
        }
    },
    data() {
        return {
            items: [],
            loadedData: Object.fromEntries(this.fields.map(field => [field, ''])),
            activeItem: null,
            activeDeleteId: null,
        };
    },
    created() {
        this.fetchData();
    },
    methods: {
        async fetchData() {
            const url = 'http://localhost:8000';
            try {
                const response = await fetch(`${url}/api/${this.model}`, {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json'
                    }
                });

                if (!response.ok) {
                    throw new Error(`Response status: ${response.status}`);
                }
                const json = await response.json();
                const model = `${this.model}s`;
                this.items = json[model];

                this.loadedData = Object.fromEntries(this.fields.map(field => [field, '']));
                this.$emit(`${this.model}`, this.items);
            } catch (error) {
                console.error(`Error fetching ${this.model}:`, error);
            }
        },
        openEditModal(item) {
            this.activeItem = item;
            this.$nextTick(() => {
                const modalElement = document.getElementById('editModal');
                const modal = new bootstrap.Modal(modalElement);
                modal.show();
            });
        },
        closeEditModal() {
            this.activeItem = null;
        },
        openDeleteModal(id) {
            this.activeDeleteId = id;
            this.$nextTick(() => {
                const modalElement = document.getElementById('deleteModal');
                const modal = new bootstrap.Modal(modalElement);
                modal.show();
            });
        },
        closeDeleteModal() {
            this.activeDeleteId = null;
        }
    },
    computed: {
        computedData() {
            return this.loadedData;
        }
    }
};
</script>

<style scoped>
.row {
    font-weight: bold;
    font-size: 1.1em;
    background-color: #c291e2;
    margin-top: 1em;
    border-top-left-radius: 0.5rem;
    border-top-right-radius: 0.5rem;
}

.info {
    display: flex;
    justify-content: space-between;
    text-align: center;
}

.data-field {
    flex: 1;
}

.buttons {
    display: flex;
    gap: 2rem;
    flex: 1;
}
</style>

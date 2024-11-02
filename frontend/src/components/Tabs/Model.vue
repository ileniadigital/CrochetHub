<template>
    <!-- Add modal -->
    <Add :model="model" :data="computedData" :fields="fields" @added="fetchData" @update="updateData" />

    <!-- Headings -->
    <!-- Bootstrap styling -->
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
        <li class="list-group-item" v-for="item in items" :key="item.id">
            <div class="info">
                <!-- Display data fields based on fields-->
                <div v-for="field in fields" :key="field" class="data-field item">
                    <template v-if="field === 'link'">
                        <a :href="item[field]">View</a>
                    </template>
                    <template v-else>
                        {{ item[field] }}
                    </template>
                </div>
                <div class="buttons">
                    <Edit :model="model" :data="item" :headers="headers" @edited="fetchData" />
                    <Delete :model="model" :id="item.id" @deleted="fetchData" />
                </div>
            </div>
        </li>
    </ul>
</template>

<script>
import axios from 'axios';
import Add from '../Action/Add.vue';
import Edit from '../Action/Edit.vue';
import Delete from '../Action/Delete.vue';

const url = 'http://localhost:8000';

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
            loadedData: Object.fromEntries(this.fields.map(field => [field, '']))
        };
    },
    created() {
        this.fetchData();
    },
    methods: {
        async fetchData() {
            try {
                console.log(`${url}/api/${this.model}`);
                const response = await axios.get(`${url}/api/${this.model}`);
                let model = `${this.model}s`;
                this.items = response.data[model];
                console.log(`Fetched ${this.model}:`, this.items);

                // Initialize loadedData based on fields
                this.loadedData = Object.fromEntries(this.fields.map(field => [field, '']));
                this.$emit(`${this.model}`, this.items);
            } catch (error) {
                console.error(`Error fetching ${this.model}:`, error);
            }
        },
        updateData() {
            this.loadedData = { ...this.items[0] };
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

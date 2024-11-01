<template>
    <!-- Add modal -->
    <!-- <button class="btn btn-primary" type="button" @click="addModal">
        <i class="bi bi-plus-square-fill">
            <p>Add new {{ model }}</p>
        </i>
    </button> -->
    <Add :model="model" :data="computedData" @added="fetchYarns" @update="updateData" />
    <!-- Properties headings-->
    <div class="container text-center">
        <div class="row">
            <div class="col">
                Brand
            </div>
            <div class="col">
                Material
            </div>
            <div class="col">
                Colour
            </div>
            <div class="col">
                Weight
            </div>
            <div class="col">
                Price
            </div>
            <div class="col">
                Yardage
            </div>
            <div class="col">
                Hook Size
            </div>
            <div class="col"></div>
        </div>
    </div>
    <!-- Yarn data -->
    <ul class="list-group">
        <li class="list-group-item" v-for="yarn in yarns" :key="yarn.id">
            <div class="info">
                <div class="brand">{{ yarn.brand }}</div>
                <div class="material">{{ yarn.material }}</div>
                <div class="colour">{{ yarn.colour }}</div>
                <div class="weight">{{ yarn.weight }}g</div>
                <div class="price">£{{ yarn.price }}</div>
                <div class="yardage">{{ yarn.yardage }}m</div>
                <div class="hook">{{ yarn.hook_size }}mm</div>
                <!-- Edit button -->
                <div class="buttons">
                    <Edit :data="yarn" @edited="fetchYarns" />
                    <!-- Delete button -->
                    <Delete :id="yarn.id" @deleted="fetchYarns" />
                </div>
            </div>
        </li>
    </ul>
</template>

<script>
import axios from 'axios';
const url = 'http://localhost:8000';
import Add from './Action/Add.vue';
import Edit from './Action/Edit.vue';
import Delete from './Action/Delete.vue';

export default {
    components: {
        Add,
        Edit,
        Delete
    },
    data() {
        return {
            yarns: [],
            model: 'Yarn',
            loadedData: {
                brand: '',
                material: '',
                colour: '',
                weight: 0,
                price: 0,
                yardage: 0,
                hook_size: 0,
            },
        };
    },
    created() {
        this.fetchYarns();
    },
    methods: {
        async fetchYarns() {

            try {
                const response = await axios.get(`${url}/api/yarn`);
                this.yarns = response.data.yarns;
                console.log(this.yarns);
                this.loadedData = { brand: '', material: '', colour: '', weight: 0, price: 0, yardage: 0, hook_size: 0 };
                console.log('loadedData at fetching:', this.loadedData);
                this.$emit('yarns', this.yarns); // Emit yarns to Tab
            } catch (error) {
                console.error('Error fetching yarn:', error);
            }
        },
        updateData() {
            this.loadedData = { ...this.yarns[0] };
            console.log('loadedData:', this.loadedData);
            console.log("updating data")

        }
    },
    computed: {
        computedData() {
            return this.loadedData;
        }
    }
}
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

.brand,
.material,
.colour,
.weight,
.price,
.yardage,
.hook,
.buttons {
    flex: 1;
}

.buttons {
    display: flex;
    gap: 2rem;
}

.brand {
    font-weight: bold;
}

.material {
    font-style: italic;
}
</style>
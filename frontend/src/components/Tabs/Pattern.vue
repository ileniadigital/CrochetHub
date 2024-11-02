<template>
    <!-- Add modal -->
    <Add :model="model" :data="computedData" @added="fetchPatterns" @update="updateData" />
    <!-- Properties headings-->
    <div class="container text-center">
        <div class="row">
            <div class="col">
                Title
            </div>
            <div class="col">
                Description
            </div>
            <div class="col">
                Published
            </div>
            <div class="col">
                Link
            </div>
            <div class="col">
                Transcript
            </div>
            <div class="col"></div>
        </div>
    </div>
    <!-- Pattern data -->
    <ul class="list-group">
        <li class="list-group-item" v-for="pattern in patterns" :key="pattern.id">
            <div class="info">
                <div class="title">{{ pattern.title }}</div>
                <div class="description">{{ pattern.description }}</div>
                <div class="published">{{ pattern.published }}</div>
                <div class="link"><a :href="pattern.link" target="_blank">View</a></div>
                <div class="transcript">{{ pattern.transcript }}</div>
                <!-- Edit button -->
                <div class="buttons">
                    <Edit :model="model" :data="pattern" @edited="fetchPatterns" />
                    <!-- Delete button -->
                    <Delete :model="model" :id="pattern.id" @deleted="fetchPatterns" />
                </div>
            </div>
        </li>
    </ul>
</template>

<script>
import axios from 'axios';
const url = 'http://localhost:8000';
import Add from '../Action/Add.vue';
import Edit from '../Action/Edit.vue';
import Delete from '../Action/Delete.vue';
export default {
    components: {
        Add,
        Edit,
        Delete
    },
    data() {
        return {
            patterns: [],
            model: 'pattern',
            loadedData: {
                title: '',
                description: '',
                published: new Date(),
                link: '',
                transcript: ''
            },
        };
    },
    created() {
        this.fetchPatterns();
    },
    methods: {
        async fetchPatterns() {
            try {
                const response = await axios.get(`${url}/api/pattern`);
                this.patterns = response.data.patterns;
                console.log("Patterns:", this.patterns);
                this.loadedData = { title: '', description: '', published: new Date(), link: '', transcript: '' };
                console.log('loadedData at fetching:', this.loadedData);
                this.$emit('patterns', this.patterns); // Emit patterns to Tab
            } catch (error) {
                console.error('Error fetching patterns:', error);
            }
        },
        updateData() {
            this.loadedData = { ...this.patterns[0] };
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

.title,
.description,
.published,
.link,
.transcript,
.buttons {
    flex: 1;
}

.buttons {
    display: flex;
    gap: 2rem;
}

.title {
    font-weight: bold;
}

.description {
    font-style: italic;
}
</style>

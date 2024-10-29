<template>
    <!-- Yarn data -->
    <h3>Yarns</h3> 
    <ul class="list-group"> 
        <li class="list-group-item" v-for="yarn in yarns" :key="yarn.id">
            {{ yarn.brand }} - {{ yarn.colour }}
        </li> 
    </ul>
</template>

<script>
    import axios from 'axios';
    const base = 'http://localhost:8000/';

    export default {
        data() {
            return {
                yarns: []
            };
        },
        created() {
            this.fetchYarns();
        },
        methods: {
            async fetchYarns() {
                try {
                    const response = await axios.get(`${base}/api/yarns`);
                    this.yarns = response.data.yarns;
                    this.$emit('yarns', this.yarns); // Emit yarns to Tab
                } catch (error) {
                    console.error('Error fetching yarn:', error);
                }
            }
        }
    }
</script>
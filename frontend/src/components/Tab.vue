<template>
    <!-- Navigation tabs -->
    <ul class="nav nav-tabs">
        <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Yarn</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="#">Pattern</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="#">PatternYarn</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" aria-disabled="true">User</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" aria-disabled="true">Project</a>
        </li>
</ul>

<!-- Yarn data -->
<h3>Yarns</h3> 
<ul> 
    <li v-for="yarn in yarns" :key="yarn.id">{{ yarn.brand }} - {{ yarn.colour }}
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
                    console.log('Yarns:', this.yarns);
                } catch (error) {
                    console.error('Error fetching yarn:', error);
                }
            }
        }
    }
</script>
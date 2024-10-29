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

<!-- Data -->
<div class="tab-content">
    <div class="tab-pane fade show active" id="home-tab-pane" role="tabpanel" aria-labelledby="home-tab" tabindex="0">
        <Yarn :yarns="yarns"/>
    </div>
</div>
<!-- <h3>Yarns</h3> 
<ul> 
    <li v-for="yarn in yarns" :key="yarn.id">{{ yarn.brand }} - {{ yarn.colour }}
    </li> 
</ul> -->
</template>

<script>
    import axios from 'axios';
    import Yarn from './Yarn.vue';
    const base = 'http://localhost:8000/';

    export default {
        components: {
            Yarn
        },
        data() {
            return {
                yarns: []
            };
        },
        created() {
           // this.fetchYarns();
        },
        methods: {
            handleYarns(yarns) {
                this.yarns = yarns;
            },
        }
    }
</script>
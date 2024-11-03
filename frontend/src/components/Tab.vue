<template>
    <!-- Navigation tabs -->
    <ul class="nav nav-tabs">
        <li class="nav-item">
            <a class="nav-link" :class="{ active: activeTab === 'yarn' }" @click="setActiveTab('yarn')">Yarn</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" :class="{ active: activeTab === 'pattern' }"
                @click="setActiveTab('pattern')">Pattern</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" :class="{ active: activeTab === 'patteryarn' }"
                @click="setActiveTab('patternyarn')">PatternYarn</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" :class="{ active: activeTab === 'user' }" @click="setActiveTab('user')">User</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" :class="{ active: activeTab === 'project' }"
                @click="setActiveTab('project')">Project</a>
        </li>
    </ul>

    <!-- Tab content -->
    <div class="tab-content">
        <!-- Yarn -->
        <div class="tab-pane fade" :class="{ 'show active': activeTab === 'yarn' }" v-if="activeTab === 'yarn'">
            <Model ref="yarn" :model="'yarn'"
                :fields="['brand', 'material', 'colour', 'weight', 'price', 'yardage', 'hook_size']"
                :headers="['Brand', 'Material', 'Colour', 'Weight', 'Price', 'Yardage', 'Hook Size']" />
        </div>
        <!-- Pattern -->
        <div class="tab-pane fade" :class="{ 'show active': activeTab === 'pattern' }" v-if="activeTab === 'pattern'">
            <Model ref="pattern" :model="'pattern'"
                :fields="['title', 'description', 'published', 'link', 'transcript']"
                :headers="['Title', 'Description', 'Published', 'Link', 'Transcript']" />
        </div>
        <!-- PatternYarn -->
        <div class="tab-pane fade" :class="{ 'show active': activeTab === 'patternyarn' }"
            v-if="activeTab === 'patternyarn'">
            <Model ref="patternyarn" :model="'patternyarn'" :fields="['pattern', 'yarn', 'quantity']"
                :headers="['Pattern', 'Yarn', 'Quantity']" />
        </div>
        <!-- User -->
        <div class="tab-pane fade" :class="{ 'show active': activeTab === 'user' }" v-if="activeTab === 'user'">
            <Model ref="user" :model="'user'" :fields="['username', 'email', 'password']"
                :headers="['Username', 'Email', 'Password']" />
        </div>
        <!-- Project -->
        <div class="tab-pane fade" :class="{ 'show active': activeTab === 'project' }" v-if="activeTab === 'project'">
            <Model ref="project" :model="'project'"
                :fields="['title', 'description', 'pattern', 'user', 'date_started', 'finished', 'date_finished', 'notes']"
                :headers="['Title', 'Description', 'Pattern', 'User', 'Date Started', 'Finished', 'Date Finished', 'Notes']" />
        </div>
    </div>
</template>

<script>
import Model from './Tabs/Model.vue';

export default {
    components: {
        Model
    },
    data() {
        return {
            activeTab: 'yarn'
        };
    },
    methods: {
        setActiveTab(tab) {
            this.activeTab = tab;
            if (this.$refs[tab]) {
                this.$refs[tab].fetchData();
            }
        }
    }
};

</script>

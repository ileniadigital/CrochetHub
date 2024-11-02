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
        <div class="tab-pane fade" :class="{ 'show active': activeTab === 'yarn' }">
            <Model :model="'yarn'" :fields="['brand', 'material', 'colour', 'weight', 'price', 'yardage', 'hook_size']"
                :headers="['Brand', 'Material', 'Colour', 'Weight', 'Price', 'Yardage', 'Hook Size']" />
        </div>
        <!-- Pattern -->
        <div class="tab-pane fade" :class="{ 'show active': activeTab === 'pattern' }">
            <Model :model="'pattern'" :fields="['title', 'description', 'published', 'link', 'transcript']"
                :headers="['Title', 'Description', 'Published', 'Link', 'Transcript']" />
        </div>
        <!-- PatternYarn -->
        <div class="tab-pane fade" :class="{ 'show active': activeTab === 'patternyarn' }">
            <Model :model="'patternyarn'" :fields="['pattern', 'yarn', 'quantity']"
                :headers="['Pattern', 'Yarn', 'Quantity']" />
        </div>
        <!-- User -->
        <div class="tab-pane fade" :class="{ 'show active': activeTab === 'user' }">
            <Model :model="'user'" :fields="['username', 'email', 'password']"
                :headers="['Username', 'Email', 'Password']" />
        </div>
        <!-- Project -->
        <div class="tab-pane fade" :class="{ 'show active': activeTab === 'project' }">
            <Model :model="'project'"
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
            console.log(this.activeTab);
        }
    }
};
</script>

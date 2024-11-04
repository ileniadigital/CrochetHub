<template>
    <form @submit.prevent="submitForm">
        <div v-for="(value, key) in formData" :key="key" class="mb-3">
            <label :for="key" class="form-label">{{
                key.charAt(0).toUpperCase() + key.slice(1)
                }}</label>

            <!-- Dropdowns for yarn and pattern -->
            <!-- Specific for PatternYarn -->
            <select v-if="key === 'yarn'" v-model="formData[key]" class="form-control">
                <option value="" disabled>Select Yarn</option>
                <option v-for="yarn in yarnOptions" :key="yarn.id" :value="yarn.id">
                    {{ yarn.brand }} - {{ yarn.colour }}
                </option>
            </select>

            <select v-else-if="key === 'pattern'" v-model="formData[key]" class="form-control">
                <option value="" disabled>Select Pattern</option>
                <option v-for="pattern in patternOptions" :key="pattern.id" :value="pattern.id">
                    {{ pattern.title }}
                </option>
            </select>

            <!-- Other inputs for string, number, and textarea fields -->
            <input v-else-if="typeof value === 'string' && value.length <= 100" type="text" :id="key"
                v-model="formData[key]" class="form-control" />
            <input v-else-if="typeof value === 'number'" type="number" :id="key" v-model="formData[key]"
                class="form-control" />
            <textarea v-else-if="typeof value === 'string' && value.length > 100" :id="key" v-model="formData[key]"
                class="form-control"></textarea>
        </div>
    </form>
</template>

<script>
export default {
    props: {
        edit: {
            type: Boolean,
            default: false,
        },
        data: {
            type: Object,
            required: true,
            default: () => ({}),
        },
        model: {
            type: String,
            required: true,
        },
    },
    data() {
        return {
            formData: {},
            yarnOptions: [],
            patternOptions: [],
        };
    },
    created() {
        this.createFormData();
        this.fetchOptions(); // Fetch options when the component is created
    },
    watch: {
        model: {
            handler: 'fetchOptions', // Refetch options if the model changes
            immediate: true,
        },
    },
    methods: {
        createFormData() {
            if (this.edit) {
                this.formData = { ...this.data };
            } else {
                this.formData = { ...this.data };
                for (const key in this.data) {
                    this.formData[key] = "";
                }
            }
            console.log("Form data created:", this.formData);
        },
        async fetchOptions() {
            // Check if model is pattern or patternyarn
            if (this.model.toLowerCase() === 'project' || this.model.toLowerCase() === 'patternyarn') {
                await this.fetchYarnOptions();
                await this.fetchPatternOptions();
            }
        },
        async fetchYarnOptions() {
            try {
                console.log("Fetching yarn options...");
                const response = await fetch('http://localhost:8000/api/yarn');
                const data = await response.json();
                this.yarnOptions = data.yarns;
                console.log("Yarn options fetched:", this.yarnOptions);
            } catch (error) {
                console.error("Failed to fetch yarn options:", error);
            }
        },
        async fetchPatternOptions() {
            try {
                console.log("Fetching pattern options...");
                const response = await fetch('http://localhost:8000/api/pattern');
                const data = await response.json();
                this.patternOptions = data.patterns;
                console.log("Pattern options fetched:", this.patternOptions);
            } catch (error) {
                console.error("Failed to fetch pattern options:", error);
            }
        },
        submitForm() {
            console.log("Form submitted with data:", this.formData);
            this.$emit("submit", this.formData);
        },
    },
};
</script>

<style>
.mb-3 {
    display: flex;
    flex-direction: column;
    margin-bottom: 1em;
}

.form-label {
    text-align: left;
    margin-bottom: 0.5em;
    font-weight: bold;
}

.form-control {
    width: 100%;
    box-sizing: border-box;
}
</style>

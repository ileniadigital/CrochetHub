<template>
    <form @submit.prevent="submitForm">
        <div v-for="(value, key) in formData" :key="key" class="mb-3">
            <label :for="key" class="form-label">{{
                key.charAt(0).toUpperCase() + key.slice(1)
                }}</label>
            <input v-if="typeof value === 'string' && value.length <= 100" type="text" :id="key" v-model="formData[key]"
                class="form-control" />
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
    },
    data() {
        return {
            formData: {},
        };
    },
    created() {
        this.createFormData();
    },
    beforeDestroy() {
        this.formData = {};
    },
    methods: {
        createFormData() {
            if (this.edit) {
                this.formData = { ...this.data };
            } else {
                for (const key in this.data) {
                    this.formData[key] = "";
                }
                console.log("formData:", this.formData);
            }
        },
        submitForm() {
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

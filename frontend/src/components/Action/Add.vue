<template>
    <div>
        <!-- Action button -->
        <button @click="updateData" class="btn btn-primary" type="button" data-bs-toggle="modal"
            data-bs-target="#addModal" id="addButton">
            <i class="bi bi-plus-square-fill"></i>
            <p>Add new {{ model }}</p>
        </button>

        <!-- Modal -->
        <div class="modal fade" id="addModal" tabindex="-1" aria-labelledby="addModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="addModalLabel">Add</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <!-- Pass default fields to ActionForm when adding new data -->
                        <ActionForm ref="actionForm" :edit="false" :data="computedData" @submit="formSubmit" />
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">
                            Close
                        </button>
                        <button type="button" class="btn btn-primary" @click="addData" data-bs-dismiss="modal">
                            Add new
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import ActionForm from "./ActionForm.vue";
const url = "http://localhost:8000";

export default {
    components: {
        ActionForm,
    },
    data() {
        return {
            loadedData: {},
        };
    },
    props: {
        model: {
            type: String,
            required: true,
        },
        data: {
            type: Object,
            required: true,
        },
        fields: {
            type: Array,
            required: true,
        },
    },
    methods: {
        updateData() {
            console.log("updating data");
            console.log("loadedData:", this.data);
            this.$emit('update');
        },
        async addData() {
            // Call the submitForm method of the ActionForm component
            this.$refs.actionForm.submitForm();
        },
        formSubmit(formData) {
            // Now you have the form data to send in the POST request
            this.submitData(formData);
        },
        async submitData(formData) {
            try {
                console.log(`${url}/api/${this.model}`);
                const response = await axios.post(`${url}/api/${this.model}`, formData);
                this.$emit("added", response.data);
                console.log("Item added", response.data);
            } catch (error) {
                console.error("Error during POST request:", error);
            }
        },
    },
    computed: {
        computedData() {
            // Initialise an empty object with the fields as keys
            return Object.fromEntries(this.fields.map(field => [field, '']));
        }
    }
};
</script>

<style>
#addButton {
    margin-top: 1em;
    display: flex;
    flex-direction: row;
    gap: 1rem;
}
</style>

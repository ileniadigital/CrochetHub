<template>
    <div>
        <!-- Action button -->
        <button @click="updateData" class="btn btn-primary" type="button" data-bs-toggle="modal"
            data-bs-target="#addModal">
            <i class="bi bi-plus-square-fill">
                <p>Add new {{ model }}</p>
            </i>
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
                        <ActionForm ref="actionForm" :edit="false" :data="data" @submit="formSubmit" />
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">
                            Close
                        </button>
                        <button type="button" class="btn btn-primary" @click="addYarn" data-bs-dismiss="modal">
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
    data() {
        return {
            data: {
                type: Object,
                required: true,
            },
        };
    },
    components: {
        ActionForm,
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
    },
    methods: {
        updateData() {
            console.log("updating data");
            this.$emit('update');
        },
        async addYarn() {
            // Call the submitForm method of the ActionForm component
            this.$refs.actionForm.submitForm();
        },
        formSubmit(formData) {
            // Now you have the form data to send in the POST request
            this.submitYarnData(formData);
        },
        async submitYarnData(formData) {
            try {
                const response = await axios.post(`${url}/api/yarn`, formData);
                this.$emit("added", response.data);
                console.log("Item added", response.data);
            } catch (error) {
                console.error("Error during POST request:", error);
            }
        },
    },
};
</script>

<style></style>

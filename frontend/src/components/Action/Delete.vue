<template>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.css">
    <!-- Action button -->
    <button class="btn btn-danger" type="button" data-bs-toggle="modal" data-bs-target="#deleteModal">
        <i class="bi bi-trash-fill"></i>
    </button>

    <!-- Modal -->
    <div class="modal fade" id="deleteModal" tabindex="-1" aria-labelledby="deleteModal" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="deleteModalLabel">Delete</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <p>Are you sure you want to delete this?</p>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-danger" @click="confirmDelete"
                        data-bs-dismiss="modal">Delete</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

const url = 'http://localhost:8000';
export default {
    props: {
        id: {
            type: Number,
            required: true
        }
    },
    emits: ['deleted'],
    methods: {
        async confirmDelete() {
            try {
                console.log(`${url}/api/yarn/${this.id}/delete/`);
                const response = await axios.delete(`${url}/api/yarn/${this.id}/delete/`);
                console.log('Item deleted', response.data);
                this.$emit('deleted', this.id);
            } catch (error) {
                console.error('There was a problem with the delete request:', error);
            }
        }
    }
};
</script>

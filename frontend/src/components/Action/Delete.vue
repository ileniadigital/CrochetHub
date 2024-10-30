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
                    <button type="button" class="btn btn-danger" @click="confirm">Delete</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    methods: {
        confirm() {
            // TO CHANGE TO USE MODELS
            // Perform delete action here
            alert('Item deleted');
        }
    }
};
</script>

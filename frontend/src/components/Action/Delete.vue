<template>
    <div>
        <!-- Modal -->
        <div class="modal fade" id="deleteModal" tabindex="-1" aria-labelledby="deleteModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="deleteModalLabel">Delete</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"
                            @click="closeModal"></button>
                    </div>
                    <div class="modal-body">
                        Are you sure you want to delete this item?
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal"
                            @click="closeModal">Close</button>
                        <button type="button" class="btn btn-danger" @click="deleteItem"
                            data-bs-dismiss="modal">Delete</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        model: {
            type: String,
            required: true,
        },
        id: {
            type: Number,
            required: true,
        },
    },
    methods: {
        async deleteItem() {
            const url = 'http://localhost:8000';
            try {
                const response = await fetch(`${url}/api/${this.model}/${this.id}/delete/`, {
                    method: 'DELETE',
                    headers: {
                        'Content-Type': 'application/json'
                    }
                });

                if (!response.ok) {
                    throw new Error(`Response status: ${response.status}`);
                }

                this.$emit('deleted');
                console.log('Item deleted');
            } catch (error) {
                console.error('Error during DELETE request:', error);
            }
        },
        closeModal() {
            this.$emit('close');
        }
    }
};
</script>
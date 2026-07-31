<template>
    <!-- Modal -->
    <div class="modal fade" :id="id" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">{{modalTitle}}</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body text-start">
            <slot>
                No Content Provided!
            </slot>
        </div>
        <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button v-if="isModalBtnLabel" type="button" class="btn btn-primary">{{modalBtnLabel}}</button>
        </div>
        </div>
    </div>
    </div>
</template>

<script>
export default{
    props:['id','modal-title','is-modal-btn-label','modal-btn-label']
}
</script>
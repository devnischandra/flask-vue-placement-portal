<template>
    <!-- Button trigger modal -->
    <button @click="$emit('open-modal')" type="button" class="btn btn-primary" data-bs-toggle="modal" :data-bs-target="`#${id}`">
        {{triggerBtnLabel}}
    </button>
</template>

<script>
export default{
    props:['id','trigger-btn-label'],
    emits: ['open-modal']
}
</script>
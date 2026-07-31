<template>
    <div class="mx-3 mt-3 mb-3">
        <h4>Applications</h4>
        <ApplicationTable :applications="applications" />
    </div>
</template>

<script>
import ApplicationTable from '../components/ApplicationTable.vue';

export default {
    components:{
        ApplicationTable
    },
    props: ["applications"]
}
</script>
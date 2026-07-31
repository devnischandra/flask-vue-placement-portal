<template>
    <div class="mx-3 mt-3">
        <h4>Placement Drives</h4>
        <PlacementDriveTable :placement_drives="placement_drives"
        @update-placement-drive="(id, update) => $emit('update-placement-drive', id, update)" />
    </div>
</template>

<script>
import PlacementDriveTable from '../components/PlacementDriveTable.vue';

export default {
    components:{
        PlacementDriveTable
    },
    props: ["placement_drives"],
    emits:['update-placement-drive']
}
</script>
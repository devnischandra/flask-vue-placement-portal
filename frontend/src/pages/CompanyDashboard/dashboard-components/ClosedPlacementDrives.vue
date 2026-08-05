<template>
    <div class="mx-3 mt-3">
        <h4>Closed Placement Drives</h4>
        <PlacementDriveTable :placement-drives="closedPlacementDrives" />
    </div>
</template>

<script>
import PlacementDriveTable from '../table-components/PlacementDriveTable.vue';

export default {
    components:{
        PlacementDriveTable
    },
    props: ["closedPlacementDrives"]
}
</script>
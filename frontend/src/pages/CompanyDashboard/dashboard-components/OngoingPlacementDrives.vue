<template>
    <div class="mx-3 mt-3">
        <div class="d-flex justify-content-between">
            <h4>Ongoing Placement Drives</h4>
            <BaseModalTriggerButton id="create-drive" trigger-btn-label="Create Drive" />
            <BaseModal id="create-drive" modal-title="Create Placement Drive" >
                <CreatePlacementDrive @create-placement-drive="(new_placement_drive) => $emit('create-placement-drive', new_placement_drive)" />
            </BaseModal>
        </div>
    <PlacementDriveTable @update-placement-drive="(id, update) => $emit('update-placement-drive', id, update)" :placement-drives="ongoingPlacementDrives" />
    </div>
</template>

<script>
import BaseModalTriggerButton from '@/components/BaseModalTriggerButton.vue';
import BaseModal from '@/components/BaseModal.vue';
import CreatePlacementDrive from './CreatePlacementDrive.vue';
import PlacementDriveTable from '../table-components/PlacementDriveTable.vue';

export default {
    components:{
        BaseModalTriggerButton,
        BaseModal,
        CreatePlacementDrive,
        PlacementDriveTable
    },
    props: ["ongoingPlacementDrives"],
    emits:['create-placement-drive','update-placement-drive']
}
</script>
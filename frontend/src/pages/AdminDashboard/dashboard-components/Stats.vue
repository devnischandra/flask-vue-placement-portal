<template>
    <div class="mx-3 mt-3">
        <h4>Stats</h4>
        <div class="d-flex justify-content-evenly">
            <p>Total Companies: {{ stats.total_companies_count }}</p>
            <p>Total Students: {{ stats.total_students_count }}</p>
            <p>Total Placement Drives: {{ stats.total_placement_drives_count }}</p>
            <p>Total Applications: {{ stats.total_applications_count }}</p>
        </div>
    </div>
</template>

<script>
export default {
    props: ["stats"]
}
</script>
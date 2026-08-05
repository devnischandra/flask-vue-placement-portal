<template>
    <nav class="navbar bg-body-tertiary p-3">
        <div class="container-fluid">
            <a class="navbar-brand">hi, {{ current_user_name }}</a>
            <BaseButton @click="logout" type="button" btn-class="link" label="Logout" />
        </div>
    </nav>
</template>

<script>
import BaseButton from '@/components/BaseButton.vue';

export default {
    components:{
        BaseButton
    },
    props: ["current_user_name"],
    methods:{
        logout(){
            localStorage.removeItem("token")
            window.location.href = "/"
        }
    }
}
</script>
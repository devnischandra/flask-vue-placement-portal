<template>
    <nav class="navbar bg-body-tertiary p-3">
        <div class="container-fluid">
            <a class="navbar-brand">hi, {{ current_user_name }}</a>
            <form class="d-flex">
                <!-- search by: id or name -->
                <select v-model="search.search_by" class="form-select me-2">
                    <option disabled value="">Search By</option>
                    <option value="id">ID</option>
                    <option value="name">Name</option>
                </select>
                <!-- search value -->
                <input v-if="search.search_by" class="form-control me-2" type="search" placeholder="enter id or name" v-model="search.value" />
                <BaseButton v-if="search.value" class="me-2" @click="doSearch" type="button" btn-class="outline-success" label="Search" />
                <BaseButton v-if="search.value" @click="reset" type="button" btn-class="outline-secondary" label="Reset" />
            </form>
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
    emits: ["search"],
    data(){
        return{
            search:{
                is_active: false,
                search_by:"",
                value:""
            }
        }
    },
    methods:{
        logout(){
            localStorage.removeItem("token")
            window.location.href = "/"
        },
        doSearch(){
            this.search.is_active = true
            this.$emit("search", { ...this.search });
        },
        reset(){
            this.search = {
                is_active:false,
                search_by:"",
                value:""
            }
            this.$emit("search", { ...this.search });
        }
    }
}
</script>
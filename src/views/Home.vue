<template>
	<el-container>
    <el-aside width="200px">Aside</el-aside>
    <el-container>
      <el-header>
        <!-- <div v-for="route in routes" :key="route.redirect">
          <router-link class="login" tag="span" to="./login">{{route.name}}</router-link>
        </div> -->
        {{routes}}
    </el-header>
      <el-main>Main</el-main>
      <el-footer>Footer</el-footer>
    </el-container>
  </el-container>
</template>
<style>
  .el-header, .el-footer {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
  }

  .el-aside {
    background-color: #D3DCE6;
    color: #333;
    text-align: center;
    line-height: 200px;
  }

  .el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: center;
    line-height: 160px;
  }

  body > .el-container {
    margin-bottom: 40px;
  }

  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 260px;
  }

  .el-container:nth-child(7) .el-aside {
    line-height: 320px;
  }
</style>

<script>
import router from '../router'
//import { reactive, onMounted, toRefs, nextTick } from 'vue'
//import { useRouter } from 'vue-router'

export default {
  name: 'home',
  components: {
    //swiper,
    //navBar
  },
  setup() {
    //const router = useRouter()
    // const state = reactive({
    //   router: router,
    // });
  },
  data(){
    return {
      routes:router,
    }
  }
}

</script>


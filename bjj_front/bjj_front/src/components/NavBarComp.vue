<template>
  <nav class="navbar navbar-expand-lg bg-light">
  <div class="container-fluid">
    <div id='nav-front' class="d-flex">
      <img id='nav-logo' src="../assets/logo.png">
      <a class="navbar-brand text-dark" href="#">Bjj-Archive</a>
    </div>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle text-dark" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Guard
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
            <li><a class="dropdown-item text-dark" href="#">Half</a></li>
            <li><a class="dropdown-item text-dark" href="#">Single-x</a></li>
            <li><a class="dropdown-item text-dark" href="#">X</a></li>
            <li><a class="dropdown-item text-dark" href="#">Lasso</a></li>
          </ul>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle text-dark" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Skill
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
            <li><a class="dropdown-item text-dark" href="#">Triangle Chock</a></li>
            <li><a class="dropdown-item text-dark" href="#">Armbar</a></li>
            <li><a class="dropdown-item text-dark" href="#">Choke</a></li>
          </ul>
        </li>
      </ul>
      <form class="d-flex" role="search">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-dark text-dark" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>
</template>

<script>
export default {

}
</script>

<style scoped>
  #nav-front {
    margin-right: 3%;
  }
  #nav-logo {
    height: 3rem;
    margin-right: 10%;
  }
</style>
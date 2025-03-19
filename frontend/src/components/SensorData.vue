<template>
  <meta charset="utf-8">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.0/css/bulma.min.css">
  <body>
    <section class="hero is-primary">
        <div class="hero-body">
            <div class="container">
                <h1 class="title">
                    Homerunner's kaffe-ø overblik 
                </h1>
                <h2 class="subtitle">
                    Gruppe 12 projekt WIP
                </h2>
            </div>
        </div>
    </section>

    <section class="section">
        <div class="container">
            <h3 class="title">Kontor Østerågade 27</h3>
            <p>Prototype til at skabe overblik over kaffe-øen med hensigt at optimere oplevelsen på kontoret</p>
        </div>
    </section>

    <section class="section">
            <h3 class="title">Spildevand oversigt</h3>
            <div class="table">
                <table class="table is-fullwidth is-hoverable is-bordered">
                    <thead>
        <tr>
          <th>Dunk Navn</th>
          <th>Procent</th>
          <th>Vægt</th>
          <th>Progress</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="sensor in sensors" :key="sensor.id">
          <td>{{ sensor.name }}</td>
          <td>{{ sensor.percentage }}</td>
          <td>{{ sensor.weight }}</td>
          <td><progress
            :class="{
              'progress': true,
              'is-success': sensor.percentage > 0 && sensor.percentage <= 40,
              'is-warning': sensor.percentage > 40 && sensor.percentage <= 60,
              'is-danger': sensor.percentage > 60
              }"
            :value="sensor.percentage"
            max="100">
          </progress>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</section>
</body>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      sensors: [],
    };
  },
  mounted() {
    axios.get('http://localhost:5000/api/sensor-data')
      .then(response => {
        this.sensors = response.data;
      })
      .catch(error => {
        console.error('Error fetching sensor data:', error);
      });
  },
};
</script>

<style>
/* Optional component-specific styles */
.container {
  margin-top: 20px;
}

.title {
  margin-bottom: 20px;
}
</style>

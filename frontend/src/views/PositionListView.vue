<template>
  <div class="main-container gjs-grid-row">
    <!-- Left Column (Chat History) -->
    <ChatHistorySection />

    <!-- Middle Column (Workspace) -->
    <div class="middle-column gjs-grid-column">
      <MobileHeader/>
      <div id="izk92si" class="middle-content"> <!-- Scroll wrapper -->
        <h1>HR Management</h1>
        <h2 id="i8yvir5">Position List</h2>
        <!-- Action Bar -->
        <div class="action-bar gjs-grid-row">
          <div class="search gjs-grid-column">
            <input type="text" placeholder="Search Positions (Designations)..." class="shadow-border"/>
          </div>
          <div class="buttons gjs-grid-column">
            <button type="button"><i class="fa-solid fa-plus"></i> Add Position</button>
          </div>
        </div>
        <!-- Data Table -->
        <table class="data-table shadow-border">
          <thead>
            <tr>
              <th>Position Name (Designation)</th>
              <th>Description</th>
              <th>Employee Count</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Developer</td>
              <td>Software Development</td>
              <td>10</td>
              <td class="actions">
                <a href="#" title="View"><i class="fa-solid fa-eye"></i></a>
                <a href="#" title="Edit"><i class="fa-solid fa-edit"></i></a>
                <a href="#" title="Delete" class="delete"><i class="fa-solid fa-trash"></i></a>
              </td>
            </tr>
            <tr>
              <td>Tester</td>
              <td>Software Quality Assurance</td>
              <td>5</td>
              <td class="actions">
                <a href="#" title="View"><i class="fa-solid fa-eye"></i></a>
                <a href="#" title="Edit"><i class="fa-solid fa-edit"></i></a>
                <a href="#" title="Delete" class="delete"><i class="fa-solid fa-trash"></i></a>
              </td>
            </tr>
            <tr>
              <td>Manager</td>
              <td>Project/Team Management</td>
              <td>3</td>
              <td class="actions">
                <a href="#" title="View"><i class="fa-solid fa-eye"></i></a>
                <a href="#" title="Edit"><i class="fa-solid fa-edit"></i></a>
                <a href="#" title="Delete" class="delete"><i class="fa-solid fa-trash"></i></a>
              </td>
            </tr>
            <tr>
              <td>HR Executive</td>
              <td>Human Resources Operations</td>
              <td>2</td>
              <td class="actions">
                <a href="#" title="View"><i class="fa-solid fa-eye"></i></a>
                <a href="#" title="Edit"><i class="fa-solid fa-edit"></i></a>
                <a href="#" title="Delete" class="delete"><i class="fa-solid fa-trash"></i></a>
              </td>
            </tr>
            <!-- Add more placeholder rows as needed -->
          </tbody>
        </table>
        <!-- Pagination (Optional) -->
        <!--
        <div class="pagination">
          <span class="disabled">&laquo;</span>
          <span class="current">1</span>
          <a href="#">&raquo;</a>
        </div>
        -->
      </div> <!-- End middle-content -->
      <!-- Bottom Navigation -->
      <div class="bottom-nav">
        <button type="button">All Employees</button>
        <button type="button">Departments</button>
        <button type="button" class="active">Positions</button>
      </div>
    </div>

    <!-- Right Column (Tabs) -->
    <TabSection />
  </div>
</template>

<script setup>
import ChatHistorySection from '../components/ChatHistorySection.vue';
import MobileHeader from '../components/MobileHeader.vue';
import TabSection from '../components/TabSection.vue';

// Component logic goes here if needed
</script>
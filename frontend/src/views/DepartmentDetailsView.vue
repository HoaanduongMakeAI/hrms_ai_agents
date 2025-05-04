<template>
  <div class="main-container gjs-grid-row">
    <!-- Left Column (Chat History) -->
    <ChatHistorySection />

    <!-- Middle Column (Workspace) -->
    <div class="middle-column gjs-grid-column">
      <MobileHeader />
      <div id="i78t9j" class="middle-content"> <!-- Scroll wrapper -->
        <h1 id="iaqhhg">HR Management</h1>
        <h2 id="i5fenh">Department Details (Add/Edit)</h2>
        <!-- Department Form -->
        <div class="department-form">
          <!-- Department Details -->
          <div id="i2if0h" class="form-section shadow-border">
            <h3><i class="fa-solid fa-sitemap"></i> Department Information</h3>
            <div id="iaaohu" class="form-grid gjs-grid-row">
              <div class="form-group gjs-grid-column">
                <label for="department_name">Department Name</label>
                <input type="text" id="department_name" name="department_name" value="IT" class="shadow-border"/>
              </div>
              <div class="form-group gjs-grid-column">
                <label for="head_of_department" id="i2wagd">Head of Department</label>
                <select type="text" id="head_of_department" name="head_of_department" class="shadow-border">
                  <option>Trần Văn D</option>
                  <option>Nguyễn Văn A</option>
                  <!-- Populate with employees -->
                </select>
              </div>
              <div id="ihknx3" class="form-group gjs-grid-column"> <!-- Span across columns -->
                <label for="description">Description</label>
                <textarea id="description" name="description" class="shadow-border"></textarea>
              </div>
            </div>
          </div>
          <!-- Employee List Section -->
          <div id="ilylk8" class="form-section employee-list-section shadow-border">
            <h4 id="imdjkw"><i class="fa-solid fa-users"></i> Employees in Department</h4> <!-- Corrected icon -->
            <div class="employee-list-actions">
              <button type="button"><i class="fa-solid fa-user-plus"></i> Add Employee to Department</button>
            </div>
            <table class="data-table shadow-border">
              <thead>
                <tr>
                  <th id="itm5s1">Employee ID</th>
                  <th>Full Name</th>
                  <th>Designation</th>
                  <th>Action</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td id="iv4b6q">EMP/0001</td>
                  <td>Nguyễn Văn A</td>
                  <td>Developer</td>
                  <td class="actions">
                    <a href="#" title="Remove from Department" class="delete"><i class="fa-solid fa-user-minus"></i></a>
                  </td>
                </tr>
                <tr>
                  <td>EMP/0002</td>
                  <td id="ivdkms">Trần Thị B</td>
                  <td id="ie8an9">Tester</td>
                  <td class="actions">
                    <a href="#" title="Remove from Department" class="delete"><i class="fa-solid fa-user-minus"></i></a>
                  </td>
                </tr>
                <!-- Add more placeholder rows -->
              </tbody>
            </table>
          </div>
          <!-- Form Actions -->
          <div class="form-actions gjs-grid-row">
            <button type="button" class="danger"><i class="fa-solid fa-trash"></i> Delete Department</button>
            <button type="button" class="secondary"><i class="fa-solid fa-times"></i> Cancel</button>
            <button type="button" class="primary"><i class="fa-solid fa-save"></i> Save</button>
          </div>
        </div>
      </div> <!-- End middle-content -->
      <!-- Bottom Navigation -->
      <div id="iynm7a" class="bottom-nav">
        <button type="button">All Employees</button>
        <button type="button" class="active">Departments</button>
        <button type="button">Positions</button>
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
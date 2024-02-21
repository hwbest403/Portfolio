﻿//
//  DrawScene.cpp
//
//  Written for CSE4170
//  Department of Computer Science and Engineering
//  Copyright © 2022 Sogang University. All rights reserved.
//

#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <GL/glew.h>
#include <GL/freeglut.h>
#include <FreeImage/FreeImage.h>
#include "LoadScene.h"

// Begin of shader setup
#include "Shaders/LoadShaders.h"
#include "ShadingInfo.h"

extern SCENE scene;

// for simple shaders
GLuint h_ShaderProgram_simple, h_ShaderProgram_TXPS; // handle to shader program
GLint loc_ModelViewProjectionMatrix, loc_primitive_color; // indices of uniform variables

// for Phong Shading (Textured) shaders
#define NUMBER_OF_LIGHT_SUPPORTED 1
GLint loc_global_ambient_color;
loc_light_Parameters loc_light[NUMBER_OF_LIGHT_SUPPORTED];
loc_Material_Parameters loc_material;
GLint loc_ModelViewProjectionMatrix_TXPS, loc_ModelViewMatrix_TXPS, loc_ModelViewMatrixInvTrans_TXPS;
GLint loc_texture;
GLint loc_flag_texture_mapping;
GLint loc_flag_fog;

// lights in scene
Light_Parameters light[NUMBER_OF_LIGHT_SUPPORTED];

// include glm/*.hpp only if necessary
// #include <glm/glm.hpp> 
#include <glm/gtc/matrix_transform.hpp> //translate, rotate, scale, lookAt, perspective, etc.
#include <glm/gtc/matrix_inverse.hpp> // inverseTranspose, etc.
// ViewProjectionMatrix = ProjectionMatrix * ViewMatrix
glm::mat4 ViewProjectionMatrix, ViewMatrix, ProjectionMatrix;
// ModelViewProjectionMatrix = ProjectionMatrix * ViewMatrix * ModelMatrix
glm::mat4 ModelViewProjectionMatrix; // This one is sent to vertex shader when ready.
glm::mat4 ModelViewMatrix;
glm::mat3 ModelViewMatrixInvTrans;

#define TO_RADIAN 0.01745329252f  
#define TO_DEGREE 57.295779513f

#define PI 3.1415926

/*********************************  START: camera *********************************/
typedef enum {
	CAMERA_0,
	CAMERA_1,
	CAMERA_2,
	CAMERA_3,
	CAMERA_m,
	CAMERA_t,
	CAMERA_g,
	NUM_CAMERAS
} CAMERA_INDEX;

typedef struct _Camera {
	float pos[3];
	float uaxis[3], vaxis[3], naxis[3];
	float fovy, aspect_ratio, near_c, far_c, zoom;
	int move, rotation_axis;
} Camera;

Camera camera_info[NUM_CAMERAS];
Camera current_camera;

using glm::mat4;
void set_ViewMatrix_from_camera_frame(void) {
	ViewMatrix = glm::mat4(current_camera.uaxis[0], current_camera.vaxis[0], current_camera.naxis[0], 0.0f,
		current_camera.uaxis[1], current_camera.vaxis[1], current_camera.naxis[1], 0.0f,
		current_camera.uaxis[2], current_camera.vaxis[2], current_camera.naxis[2], 0.0f,
		0.0f, 0.0f, 0.0f, 1.0f);

	ViewMatrix = glm::translate(ViewMatrix, glm::vec3(-current_camera.pos[0], -current_camera.pos[1], -current_camera.pos[2]));
}

void set_current_camera(int camera_num) {
	Camera* pCamera = &camera_info[camera_num];

	memcpy(&current_camera, pCamera, sizeof(Camera));
	set_ViewMatrix_from_camera_frame();
	ProjectionMatrix = glm::perspective(camera_info[camera_num].zoom * camera_info[camera_num].fovy * TO_RADIAN, camera_info[camera_num].aspect_ratio, camera_info[camera_num].near_c, camera_info[camera_num].far_c);
	ViewProjectionMatrix = ProjectionMatrix * ViewMatrix;
}

void initialize_camera(void) {
	//orthonormal을 위해 math라이브러리 sin cos 함수를 써서 각으로 표현함.
	//CAMERA_0
	Camera* pCamera = &camera_info[CAMERA_0];
	pCamera->pos[0] = -2250.0f; pCamera->pos[1] = 650.0f; pCamera->pos[2] = 3500.0f;
	pCamera->uaxis[0] = -cos(60 * PI / 180); pCamera->uaxis[1] = -sin(60 * PI / 180); pCamera->uaxis[2] = 0.0f;
	pCamera->vaxis[0] = cos(45 * PI / 180) * cos(30 * PI / 180); pCamera->vaxis[1] = -cos(45 * PI / 180) * cos(60 * PI / 180); pCamera->vaxis[2] = sin(45 * PI / 180);
	pCamera->naxis[0] = -cos(45 * PI / 180) * cos(30 * PI / 180); pCamera->naxis[1] = cos(45 * PI / 180) * cos(60 * PI / 180); pCamera->naxis[2] = sin(45 * PI / 180);
	pCamera->move = 0;
	pCamera->zoom = 100.0f;
	pCamera->fovy = TO_RADIAN * scene.camera.fovy, pCamera->aspect_ratio = scene.camera.aspect, pCamera->near_c = 0.1f; pCamera->far_c = 30000.0f;

	//CAMERA_1
	pCamera = &camera_info[CAMERA_1];
	pCamera->pos[0] = 1500.0f; pCamera->pos[1] = 3600.0f; pCamera->pos[2] = 2000.0f;
	pCamera->uaxis[0] = -cos(30 * PI / 180); pCamera->uaxis[1] = sin(30 * PI / 180); pCamera->uaxis[2] = 0.0f;
	pCamera->vaxis[0] = -cos(60 * PI / 180) * cos(60 * PI / 180); pCamera->vaxis[1] = -cos(60 * PI / 180) * cos(30 * PI / 180); pCamera->vaxis[2] = sin(60 * PI / 180);
	pCamera->naxis[0] = cos(30 * PI / 180) * cos(60 * PI / 180); pCamera->naxis[1] = cos(30 * PI / 180) * cos(30 * PI / 180); pCamera->naxis[2] = sin(30 * PI / 180);
	pCamera->move = 0;
	pCamera->zoom = 100.0f;
	pCamera->fovy = TO_RADIAN * scene.camera.fovy, pCamera->aspect_ratio = scene.camera.aspect, pCamera->near_c = 0.1f; pCamera->far_c = 30000.0f;

	//CAMERA_2
	pCamera = &camera_info[CAMERA_2];
	pCamera->pos[0] = 1974.856567f; pCamera->pos[1] = -1588.545776f; pCamera->pos[2] = 2000.0f;
	pCamera->uaxis[0] = cos(60 * PI / 180); pCamera->uaxis[1] = sin(60 * PI / 180); pCamera->uaxis[2] = 0.0f;
	pCamera->vaxis[0] = cos(45 * PI / 180) * cos(30 * PI / 180); pCamera->vaxis[1] = -cos(45 * PI / 180) * cos(60 * PI / 180); pCamera->vaxis[2] = sin(45 * PI / 180);
	pCamera->naxis[0] = -cos(45 * PI / 180) * cos(30 * PI / 180); pCamera->naxis[1] = cos(45 * PI / 180) * cos(60 * PI / 180); pCamera->naxis[2] = sin(45 * PI / 180);
	pCamera->move = 0;
	pCamera->zoom = 100.0f;
	pCamera->fovy = TO_RADIAN * scene.camera.fovy, pCamera->aspect_ratio = scene.camera.aspect, pCamera->near_c = 0.1f; pCamera->far_c = 30000.0f;

	//CAMERA_3 : top view
	pCamera = &camera_info[CAMERA_3];
	pCamera->pos[0] = 4465.0f; pCamera->pos[1] = -2600.0f; pCamera->pos[2] = 7000.0f;
	pCamera->uaxis[0] = 1.0f; pCamera->uaxis[1] = 0.0f; pCamera->uaxis[2] = 0.0f;
	pCamera->vaxis[0] = 0.0f; pCamera->vaxis[1] = 1.0f; pCamera->vaxis[2] = 0.0f;
	pCamera->naxis[0] = 0.0f; pCamera->naxis[1] = 0.0f; pCamera->naxis[2] = 1.0f;
	pCamera->move = 0;
	pCamera->zoom = 100.0f;
	pCamera->fovy = TO_RADIAN * scene.camera.fovy, pCamera->aspect_ratio = scene.camera.aspect, pCamera->near_c = 0.1f; pCamera->far_c = 30000.0f;

	//CAMERA_m : top view
	pCamera = &camera_info[CAMERA_m];
	pCamera->pos[0] = 0.0f; pCamera->pos[1] = 0.0f; pCamera->pos[2] = 7000.0f;
	pCamera->uaxis[0] = 1.0f; pCamera->uaxis[1] = 0.0f; pCamera->uaxis[2] = 0.0f;
	pCamera->vaxis[0] = 0.0f; pCamera->vaxis[1] = 1.0f; pCamera->vaxis[2] = 0.0f;
	pCamera->naxis[0] = 0.0f; pCamera->naxis[1] = 0.0f; pCamera->naxis[2] = 1.0f;
	pCamera->move = 0;
	pCamera->zoom = 100.0f;
	pCamera->fovy = TO_RADIAN * scene.camera.fovy, pCamera->aspect_ratio = scene.camera.aspect, pCamera->near_c = 0.1f; pCamera->far_c = 30000.0f;

	//CAMERA_t : tiger view
	pCamera = &camera_info[CAMERA_t];
	pCamera->pos[0] = 0.0f; pCamera->pos[1] = -2.5f*88.0f; pCamera->pos[2] = 2.5f * 62.0f;
	pCamera->uaxis[0] = -1.0f; pCamera->uaxis[1] = 0.0f; pCamera->uaxis[2] = 0.0f;
	pCamera->vaxis[0] = 0.0f; pCamera->vaxis[1] = 0.0f; pCamera->vaxis[2] = 1.0f;
	pCamera->naxis[0] = 0.0f; pCamera->naxis[1] = 1.0f; pCamera->naxis[2] = 0.0f;
	pCamera->move = 0;
	pCamera->zoom = 100.0f;
	pCamera->fovy = TO_RADIAN * scene.camera.fovy, pCamera->aspect_ratio = scene.camera.aspect, pCamera->near_c = 0.1f; pCamera->far_c = 30000.0f;

	//CAMERA_g : tiger_g view
	pCamera = &camera_info[CAMERA_g];
	pCamera->pos[0] = 0.0f; pCamera->pos[1] = 2.5f * 100.0f; pCamera->pos[2] = 2.5f * 200.0f;
	pCamera->uaxis[0] = -1.0f; pCamera->uaxis[1] = 0.0f; pCamera->uaxis[2] = 0.0f;
	pCamera->vaxis[0] = 0.0f; pCamera->vaxis[1] = 0.0f; pCamera->vaxis[2] = 1.0f;
	pCamera->naxis[0] = 0.0f; pCamera->naxis[1] = 1.0f; pCamera->naxis[2] = 0.0f;
	pCamera->move = 0;
	pCamera->zoom = 100.0f;
	pCamera->fovy = TO_RADIAN * scene.camera.fovy, pCamera->aspect_ratio = scene.camera.aspect, pCamera->near_c = 0.1f; pCamera->far_c = 30000.0f;

	set_current_camera(CAMERA_0);
}
/*********************************  END: camera *********************************/

/******************************  START: shader setup ****************************/
// Begin of Callback function definitions
void prepare_shader_program(void) {
	int i;
	char string[256];
	ShaderInfo shader_info_simple[3] = {
		{ GL_VERTEX_SHADER, "Shaders/simple.vert" },
		{ GL_FRAGMENT_SHADER, "Shaders/simple.frag" },
		{ GL_NONE, NULL }
	};
	ShaderInfo shader_info_TXPS[3] = {
		{ GL_VERTEX_SHADER, "Shaders/Phong_Tx.vert" },
		{ GL_FRAGMENT_SHADER, "Shaders/Phong_Tx.frag" },
		{ GL_NONE, NULL }
	};

	h_ShaderProgram_simple = LoadShaders(shader_info_simple);
	loc_primitive_color = glGetUniformLocation(h_ShaderProgram_simple, "u_primitive_color");
	loc_ModelViewProjectionMatrix = glGetUniformLocation(h_ShaderProgram_simple, "u_ModelViewProjectionMatrix");

	h_ShaderProgram_TXPS = LoadShaders(shader_info_TXPS);
	loc_ModelViewProjectionMatrix_TXPS = glGetUniformLocation(h_ShaderProgram_TXPS, "u_ModelViewProjectionMatrix");
	loc_ModelViewMatrix_TXPS = glGetUniformLocation(h_ShaderProgram_TXPS, "u_ModelViewMatrix");
	loc_ModelViewMatrixInvTrans_TXPS = glGetUniformLocation(h_ShaderProgram_TXPS, "u_ModelViewMatrixInvTrans");

	loc_global_ambient_color = glGetUniformLocation(h_ShaderProgram_TXPS, "u_global_ambient_color");
	for (i = 0; i < NUMBER_OF_LIGHT_SUPPORTED; i++) {
		sprintf(string, "u_light[%d].light_on", i);
		loc_light[i].light_on = glGetUniformLocation(h_ShaderProgram_TXPS, string);
		sprintf(string, "u_light[%d].position", i);
		loc_light[i].position = glGetUniformLocation(h_ShaderProgram_TXPS, string);
		sprintf(string, "u_light[%d].ambient_color", i);
		loc_light[i].ambient_color = glGetUniformLocation(h_ShaderProgram_TXPS, string);
		sprintf(string, "u_light[%d].diffuse_color", i);
		loc_light[i].diffuse_color = glGetUniformLocation(h_ShaderProgram_TXPS, string);
		sprintf(string, "u_light[%d].specular_color", i);
		loc_light[i].specular_color = glGetUniformLocation(h_ShaderProgram_TXPS, string);
		sprintf(string, "u_light[%d].spot_direction", i);
		loc_light[i].spot_direction = glGetUniformLocation(h_ShaderProgram_TXPS, string);
		sprintf(string, "u_light[%d].spot_exponent", i);
		loc_light[i].spot_exponent = glGetUniformLocation(h_ShaderProgram_TXPS, string);
		sprintf(string, "u_light[%d].spot_cutoff_angle", i);
		loc_light[i].spot_cutoff_angle = glGetUniformLocation(h_ShaderProgram_TXPS, string);
		sprintf(string, "u_light[%d].light_attenuation_factors", i);
		loc_light[i].light_attenuation_factors = glGetUniformLocation(h_ShaderProgram_TXPS, string);
	}

	loc_material.ambient_color = glGetUniformLocation(h_ShaderProgram_TXPS, "u_material.ambient_color");
	loc_material.diffuse_color = glGetUniformLocation(h_ShaderProgram_TXPS, "u_material.diffuse_color");
	loc_material.specular_color = glGetUniformLocation(h_ShaderProgram_TXPS, "u_material.specular_color");
	loc_material.emissive_color = glGetUniformLocation(h_ShaderProgram_TXPS, "u_material.emissive_color");
	loc_material.specular_exponent = glGetUniformLocation(h_ShaderProgram_TXPS, "u_material.specular_exponent");

	loc_texture = glGetUniformLocation(h_ShaderProgram_TXPS, "u_base_texture");

	loc_flag_texture_mapping = glGetUniformLocation(h_ShaderProgram_TXPS, "u_flag_texture_mapping");
	loc_flag_fog = glGetUniformLocation(h_ShaderProgram_TXPS, "u_flag_fog");
}
/*******************************  END: shder setup ******************************/

/****************************  START: geometry setup ****************************/
#define BUFFER_OFFSET(offset) ((GLvoid *) (offset))
#define INDEX_VERTEX_POSITION	0
#define INDEX_NORMAL			1
#define INDEX_TEX_COORD			2

bool b_draw_grid = false;

//axes
GLuint axes_VBO, axes_VAO;
GLfloat axes_vertices[6][3] = {
	{ 0.0f, 0.0f, 0.0f }, { 1.0f, 0.0f, 0.0f }, { 0.0f, 0.0f, 0.0f }, { 0.0f, 1.0f, 0.0f },
	{ 0.0f, 0.0f, 0.0f }, { 0.0f, 0.0f, 1.0f }
};
GLfloat axes_color[3][3] = { { 1.0f, 0.0f, 0.0f }, { 0.0f, 1.0f, 0.0f }, { 0.0f, 0.0f, 1.0f } };

void prepare_axes(void) {
	// Initialize vertex buffer object.
	glGenBuffers(1, &axes_VBO);

	glBindBuffer(GL_ARRAY_BUFFER, axes_VBO);
	glBufferData(GL_ARRAY_BUFFER, sizeof(axes_vertices), &axes_vertices[0][0], GL_STATIC_DRAW);

	// Initialize vertex array object.
	glGenVertexArrays(1, &axes_VAO);
	glBindVertexArray(axes_VAO);

	glBindBuffer(GL_ARRAY_BUFFER, axes_VBO);
	glVertexAttribPointer(INDEX_VERTEX_POSITION, 3, GL_FLOAT, GL_FALSE, 0, BUFFER_OFFSET(0));
	glEnableVertexAttribArray(INDEX_VERTEX_POSITION);

	glBindBuffer(GL_ARRAY_BUFFER, 0);
	glBindVertexArray(0);

	fprintf(stdout, " * Loaded axes into graphics memory.\n");
}

void draw_axes(void) {
	if (!b_draw_grid)
		return;

	glUseProgram(h_ShaderProgram_simple);
	ModelViewMatrix = glm::scale(ViewMatrix, glm::vec3(8000.0f, 8000.0f, 8000.0f));
	ModelViewProjectionMatrix = ProjectionMatrix * ModelViewMatrix;
	glUniformMatrix4fv(loc_ModelViewProjectionMatrix, 1, GL_FALSE, &ModelViewProjectionMatrix[0][0]);
	glLineWidth(2.0f);
	glBindVertexArray(axes_VAO);
	glUniform3fv(loc_primitive_color, 1, axes_color[0]);
	glDrawArrays(GL_LINES, 0, 2);
	glUniform3fv(loc_primitive_color, 1, axes_color[1]);
	glDrawArrays(GL_LINES, 2, 2);
	glUniform3fv(loc_primitive_color, 1, axes_color[2]);
	glDrawArrays(GL_LINES, 4, 2);
	glBindVertexArray(0);
	glLineWidth(1.0f);
	glUseProgram(0);
}

//grid
#define GRID_LENGTH			(100)
#define NUM_GRID_VETICES	((2 * GRID_LENGTH + 1) * 4)
GLuint grid_VBO, grid_VAO;
GLfloat grid_vertices[NUM_GRID_VETICES][3];
GLfloat grid_color[3] = { 0.5f, 0.5f, 0.5f };

void prepare_grid(void) {

	//set grid vertices
	int vertex_idx = 0;
	for (int x_idx = -GRID_LENGTH; x_idx <= GRID_LENGTH; x_idx++)
	{
		grid_vertices[vertex_idx][0] = x_idx;
		grid_vertices[vertex_idx][1] = -GRID_LENGTH;
		grid_vertices[vertex_idx][2] = 0.0f;
		vertex_idx++;

		grid_vertices[vertex_idx][0] = x_idx;
		grid_vertices[vertex_idx][1] = GRID_LENGTH;
		grid_vertices[vertex_idx][2] = 0.0f;
		vertex_idx++;
	}

	for (int y_idx = -GRID_LENGTH; y_idx <= GRID_LENGTH; y_idx++)
	{
		grid_vertices[vertex_idx][0] = -GRID_LENGTH;
		grid_vertices[vertex_idx][1] = y_idx;
		grid_vertices[vertex_idx][2] = 0.0f;
		vertex_idx++;

		grid_vertices[vertex_idx][0] = GRID_LENGTH;
		grid_vertices[vertex_idx][1] = y_idx;
		grid_vertices[vertex_idx][2] = 0.0f;
		vertex_idx++;
	}

	// Initialize vertex buffer object.
	glGenBuffers(1, &grid_VBO);

	glBindBuffer(GL_ARRAY_BUFFER, grid_VBO);
	glBufferData(GL_ARRAY_BUFFER, sizeof(grid_vertices), &grid_vertices[0][0], GL_STATIC_DRAW);

	// Initialize vertex array object.
	glGenVertexArrays(1, &grid_VAO);
	glBindVertexArray(grid_VAO);

	glBindBuffer(GL_ARRAY_BUFFER, grid_VAO);
	glVertexAttribPointer(INDEX_VERTEX_POSITION, 3, GL_FLOAT, GL_FALSE, 0, BUFFER_OFFSET(0));
	glEnableVertexAttribArray(INDEX_VERTEX_POSITION);

	glBindBuffer(GL_ARRAY_BUFFER, 0);
	glBindVertexArray(0);
	fprintf(stdout, " * Loaded grid into graphics memory.\n");
}

void draw_grid(void) {
	if (!b_draw_grid)
		return;

	glUseProgram(h_ShaderProgram_simple);
	ModelViewMatrix = glm::scale(ViewMatrix, glm::vec3(100.0f, 100.0f, 100.0f));
	ModelViewProjectionMatrix = ProjectionMatrix * ModelViewMatrix;
	glUniformMatrix4fv(loc_ModelViewProjectionMatrix, 1, GL_FALSE, &ModelViewProjectionMatrix[0][0]);
	glLineWidth(1.0f);
	glBindVertexArray(grid_VAO);
	glUniform3fv(loc_primitive_color, 1, grid_color);
	glDrawArrays(GL_LINES, 0, NUM_GRID_VETICES);
	glBindVertexArray(0);
	glLineWidth(1.0f);
	glUseProgram(0);
}

//bistro_exterior
GLuint* bistro_exterior_VBO;
GLuint* bistro_exterior_VAO;
int* bistro_exterior_n_triangles;
int* bistro_exterior_vertex_offset;
GLfloat** bistro_exterior_vertices;
GLuint* bistro_exterior_texture_names;

int flag_fog;
bool* flag_texture_mapping;

void initialize_lights_and_material(void) { // follow OpenGL conventions for initialization
	int i;

	glUseProgram(h_ShaderProgram_TXPS);

	glUniform4f(loc_global_ambient_color, 0.115f, 0.115f, 0.115f, 1.0f);
	for (i = 0; i < NUMBER_OF_LIGHT_SUPPORTED; i++) {
		glUniform1i(loc_light[i].light_on, 0); // turn off all lights initially
		glUniform4f(loc_light[i].position, 0.0f, 0.0f, 1.0f, 0.0f);
		glUniform4f(loc_light[i].ambient_color, 0.0f, 0.0f, 0.0f, 1.0f);
		if (i == 0) {
			glUniform4f(loc_light[i].diffuse_color, 1.0f, 1.0f, 1.0f, 1.0f);
			glUniform4f(loc_light[i].specular_color, 1.0f, 1.0f, 1.0f, 1.0f);
		}
		else {
			glUniform4f(loc_light[i].diffuse_color, 0.0f, 0.0f, 0.0f, 1.0f);
			glUniform4f(loc_light[i].specular_color, 0.0f, 0.0f, 0.0f, 1.0f);
		}
		glUniform3f(loc_light[i].spot_direction, 0.0f, 0.0f, -1.0f);
		glUniform1f(loc_light[i].spot_exponent, 0.0f); // [0.0, 128.0]
		glUniform1f(loc_light[i].spot_cutoff_angle, 180.0f); // [0.0, 90.0] or 180.0 (180.0 for no spot light effect)
		glUniform4f(loc_light[i].light_attenuation_factors, 1.0f, 0.0f, 0.0f, 0.0f); // .w != 0.0f for no ligth attenuation
	}

	glUniform4f(loc_material.ambient_color, 0.2f, 0.2f, 0.2f, 1.0f);
	glUniform4f(loc_material.diffuse_color, 0.8f, 0.8f, 0.8f, 1.0f);
	glUniform4f(loc_material.specular_color, 0.0f, 0.0f, 0.0f, 1.0f);
	glUniform4f(loc_material.emissive_color, 0.0f, 0.0f, 0.0f, 1.0f);
	glUniform1f(loc_material.specular_exponent, 0.0f); // [0.0, 128.0]

	glUseProgram(0);
}

void initialize_flags(void) {
	flag_fog = 0;

	glUseProgram(h_ShaderProgram_TXPS);
	glUniform1i(loc_flag_fog, flag_fog);
	glUseProgram(0);
}

bool readTexImage2D_from_file(const char* filename) {
	FREE_IMAGE_FORMAT tx_file_format;
	int tx_bits_per_pixel;
	FIBITMAP* tx_pixmap, * tx_pixmap_32;

	int width, height;
	GLvoid* data;

	tx_file_format = FreeImage_GetFileType(filename, 0);
	// assume everything is fine with reading texture from file: no error checking
	tx_pixmap = FreeImage_Load(tx_file_format, filename);
	if (tx_pixmap == NULL)
		return false;
	tx_bits_per_pixel = FreeImage_GetBPP(tx_pixmap);

	//fprintf(stdout, " * A %d-bit texture was read from %s.\n", tx_bits_per_pixel, filename);
	if (tx_bits_per_pixel == 32)
		tx_pixmap_32 = tx_pixmap;
	else {
		fprintf(stdout, " * Converting texture from %d bits to 32 bits...\n", tx_bits_per_pixel);
		tx_pixmap_32 = FreeImage_ConvertTo32Bits(tx_pixmap);
	}

	width = FreeImage_GetWidth(tx_pixmap_32);
	height = FreeImage_GetHeight(tx_pixmap_32);
	data = FreeImage_GetBits(tx_pixmap_32);

	glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_BGRA, GL_UNSIGNED_BYTE, data);
	//fprintf(stdout, " * Loaded %dx%d RGBA texture into graphics memory.\n\n", width, height);

	FreeImage_Unload(tx_pixmap_32);
	if (tx_bits_per_pixel != 32)
		FreeImage_Unload(tx_pixmap);

	return true;
}

void prepare_bistro_exterior(void) {
	int n_bytes_per_vertex, n_bytes_per_triangle;
	char filename[512];

	n_bytes_per_vertex = 8 * sizeof(float); // 3 for vertex, 3 for normal, and 2 for texcoord
	n_bytes_per_triangle = 3 * n_bytes_per_vertex;

	// VBO, VAO malloc
	bistro_exterior_VBO = (GLuint*)malloc(sizeof(GLuint) * scene.n_materials);
	bistro_exterior_VAO = (GLuint*)malloc(sizeof(GLuint) * scene.n_materials);

	bistro_exterior_n_triangles = (int*)malloc(sizeof(int) * scene.n_materials);
	bistro_exterior_vertex_offset = (int*)malloc(sizeof(int) * scene.n_materials);

	flag_texture_mapping = (bool*)malloc(sizeof(bool) * scene.n_textures);

	// vertices
	bistro_exterior_vertices = (GLfloat**)malloc(sizeof(GLfloat*) * scene.n_materials);

	for (int materialIdx = 0; materialIdx < scene.n_materials; materialIdx++) {
		MATERIAL* pMaterial = &(scene.material_list[materialIdx]);
		GEOMETRY_TRIANGULAR_MESH* tm = &(pMaterial->geometry.tm);

		// vertex
		bistro_exterior_vertices[materialIdx] = (GLfloat*)malloc(sizeof(GLfloat) * 8 * tm->n_triangle * 3);

		int vertexIdx = 0;
		for (int triIdx = 0; triIdx < tm->n_triangle; triIdx++) {
			TRIANGLE tri = tm->triangle_list[triIdx];
			for (int triVertex = 0; triVertex < 3; triVertex++) {
				bistro_exterior_vertices[materialIdx][vertexIdx++] = tri.position[triVertex].x;
				bistro_exterior_vertices[materialIdx][vertexIdx++] = tri.position[triVertex].y;
				bistro_exterior_vertices[materialIdx][vertexIdx++] = tri.position[triVertex].z;

				bistro_exterior_vertices[materialIdx][vertexIdx++] = tri.normal_vetcor[triVertex].x;
				bistro_exterior_vertices[materialIdx][vertexIdx++] = tri.normal_vetcor[triVertex].y;
				bistro_exterior_vertices[materialIdx][vertexIdx++] = tri.normal_vetcor[triVertex].z;

				bistro_exterior_vertices[materialIdx][vertexIdx++] = tri.texture_list[triVertex][0].u;
				bistro_exterior_vertices[materialIdx][vertexIdx++] = tri.texture_list[triVertex][0].v;
			}
		}

		// # of triangles
		bistro_exterior_n_triangles[materialIdx] = tm->n_triangle;

		if (materialIdx == 0)
			bistro_exterior_vertex_offset[materialIdx] = 0;
		else
			bistro_exterior_vertex_offset[materialIdx] = bistro_exterior_vertex_offset[materialIdx - 1] + 3 * bistro_exterior_n_triangles[materialIdx - 1];

		glGenBuffers(1, &bistro_exterior_VBO[materialIdx]);

		glBindBuffer(GL_ARRAY_BUFFER, bistro_exterior_VBO[materialIdx]);
		glBufferData(GL_ARRAY_BUFFER, bistro_exterior_n_triangles[materialIdx] * 3 * n_bytes_per_vertex,
			bistro_exterior_vertices[materialIdx], GL_STATIC_DRAW);

		// As the geometry data exists now in graphics memory, ...
		free(bistro_exterior_vertices[materialIdx]);

		// Initialize vertex array object.
		glGenVertexArrays(1, &bistro_exterior_VAO[materialIdx]);
		glBindVertexArray(bistro_exterior_VAO[materialIdx]);

		glBindBuffer(GL_ARRAY_BUFFER, bistro_exterior_VBO[materialIdx]);
		glVertexAttribPointer(INDEX_VERTEX_POSITION, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(float), BUFFER_OFFSET(0));
		glEnableVertexAttribArray(INDEX_VERTEX_POSITION);
		glVertexAttribPointer(INDEX_NORMAL, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(float), BUFFER_OFFSET(3 * sizeof(float)));
		glEnableVertexAttribArray(INDEX_NORMAL);
		glVertexAttribPointer(INDEX_TEX_COORD, 2, GL_FLOAT, GL_FALSE, 8 * sizeof(float), BUFFER_OFFSET(6 * sizeof(float)));
		glEnableVertexAttribArray(INDEX_TEX_COORD);

		glBindBuffer(GL_ARRAY_BUFFER, 0);
		glBindVertexArray(0);

		if ((materialIdx > 0) && (materialIdx % 100 == 0))
			fprintf(stdout, " * Loaded %d bistro exterior materials into graphics memory.\n", materialIdx / 100 * 100);
	}
	fprintf(stdout, " * Loaded %d bistro exterior materials into graphics memory.\n", scene.n_materials);

	// textures
	bistro_exterior_texture_names = (GLuint*)malloc(sizeof(GLuint) * scene.n_textures);
	glGenTextures(scene.n_textures, bistro_exterior_texture_names);

	for (int texId = 0; texId < scene.n_textures; texId++) {
		glActiveTexture(GL_TEXTURE0 + texId);
		glBindTexture(GL_TEXTURE_2D, bistro_exterior_texture_names[texId]);

		bool bReturn = readTexImage2D_from_file(scene.texture_file_name[texId]);

		if (bReturn) {
			glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
			glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
			glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
			glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);
			glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE);
			flag_texture_mapping[texId] = true;
		}
		else {
			flag_texture_mapping[texId] = false;
		}

		glBindTexture(GL_TEXTURE_2D, 0);
	}
	fprintf(stdout, " * Loaded bistro exterior textures into graphics memory.\n\n");
	
	free(bistro_exterior_vertices);
}

void draw_bistro_exterior(void) {
	glUseProgram(h_ShaderProgram_TXPS);
	ModelViewMatrix = ViewMatrix;
	ModelViewProjectionMatrix = ProjectionMatrix * ModelViewMatrix;
	ModelViewMatrixInvTrans = glm::transpose(glm::inverse(glm::mat3(ModelViewMatrix)));

	glUniformMatrix4fv(loc_ModelViewProjectionMatrix_TXPS, 1, GL_FALSE, &ModelViewProjectionMatrix[0][0]);
	glUniformMatrix4fv(loc_ModelViewMatrix_TXPS, 1, GL_FALSE, &ModelViewMatrix[0][0]);
	glUniformMatrix3fv(loc_ModelViewMatrixInvTrans_TXPS, 1, GL_FALSE, &ModelViewMatrixInvTrans[0][0]);

	for (int materialIdx = 0; materialIdx < scene.n_materials; materialIdx++) {
		// set material
		glUniform4fv(loc_material.ambient_color, 1, scene.material_list[materialIdx].shading.ph.ka);
		glUniform4fv(loc_material.diffuse_color, 1, scene.material_list[materialIdx].shading.ph.kd);
		glUniform4fv(loc_material.specular_color, 1, scene.material_list[materialIdx].shading.ph.ks);
		glUniform1f(loc_material.specular_exponent, scene.material_list[materialIdx].shading.ph.spec_exp);
		glUniform4fv(loc_material.emissive_color, 1, scene.material_list[materialIdx].shading.ph.kr);

		int texId = scene.material_list[materialIdx].diffuseTexId;
		glUniform1i(loc_texture, texId);
		glUniform1i(loc_flag_texture_mapping, flag_texture_mapping[texId]);

		glEnable(GL_TEXTURE_2D);
		glActiveTexture(GL_TEXTURE0 + texId);
		glBindTexture(GL_TEXTURE_2D, bistro_exterior_texture_names[texId]);

		glBindVertexArray(bistro_exterior_VAO[materialIdx]);
		glDrawArrays(GL_TRIANGLES, 0, 3 * bistro_exterior_n_triangles[materialIdx]);

		glBindTexture(GL_TEXTURE_2D, 0);
		glBindVertexArray(0);
	}
	glUseProgram(0);
}
//

void My_glTexImage2D_from_file(const char* filename) {
	FREE_IMAGE_FORMAT tx_file_format;
	int tx_bits_per_pixel;
	FIBITMAP* tx_pixmap, * tx_pixmap_32;

	int width, height;
	GLvoid* data;

	tx_file_format = FreeImage_GetFileType(filename, 0);
	// assume everything is fine with reading texture from file: no error checking
	tx_pixmap = FreeImage_Load(tx_file_format, filename);
	tx_bits_per_pixel = FreeImage_GetBPP(tx_pixmap);

	fprintf(stdout, " * A %d-bit texture was read from %s.\n", tx_bits_per_pixel, filename);
	if (tx_bits_per_pixel == 32)
		tx_pixmap_32 = tx_pixmap;
	else {
		fprintf(stdout, " * Converting texture from %d bits to 32 bits...\n", tx_bits_per_pixel);
		tx_pixmap_32 = FreeImage_ConvertTo32Bits(tx_pixmap);
	}

	width = FreeImage_GetWidth(tx_pixmap_32);
	height = FreeImage_GetHeight(tx_pixmap_32);
	data = FreeImage_GetBits(tx_pixmap_32);

	glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_BGRA, GL_UNSIGNED_BYTE, data);
	fprintf(stdout, " * Loaded %dx%d RGBA texture into graphics memory.\n\n", width, height);

	FreeImage_Unload(tx_pixmap_32);
	if (tx_bits_per_pixel != 32)
		FreeImage_Unload(tx_pixmap);
}

int read_geometry(GLfloat** object, int bytes_per_primitive, char* filename) {
	int n_triangles;
	FILE* fp;

	// fprintf(stdout, "Reading geometry from the geometry file %s...\n", filename);
	fp = fopen(filename, "rb");
	if (fp == NULL) {
		fprintf(stderr, "Cannot open the object file %s ...", filename);
		return -1;
	}
	fread(&n_triangles, sizeof(int), 1, fp);
	*object = (float*)malloc(n_triangles * bytes_per_primitive);
	if (*object == NULL) {
		fprintf(stderr, "Cannot allocate memory for the geometry file %s ...", filename);
		return -1;
	}

	fread(*object, bytes_per_primitive, n_triangles, fp);
	// fprintf(stdout, "Read %d primitives successfully.\n\n", n_triangles);
	fclose(fp);

	return n_triangles;
}

#define LOC_VERTEX 0
#define LOC_NORMAL 1
#define LOC_TEXCOORD 2

// texture stuffs
#define N_TEXTURES_USED 2
#define TEXTURE_ID_FLOOR 0
#define TEXTURE_ID_TIGER 1
GLuint texture_names[N_TEXTURES_USED];

//각 물체의 frame, angle, time 변수 및 flag

int cur_frame_tiger = 0, cur_frame_spider = 0, cur_frame_wolf = 0;
float rotation_angle_tiger = 0.0f, rotation_angle_spider = 0.0f, rotation_angle_wolf = 0.0f;

unsigned int timestamp_scene_tiger = 0, timestamp_scene_spider = 0, timestamp_scene_wolf = 0; // the global clock in the scene
int move_flag = 1;
int jump_flag = 0;
int big_flag = 0;
int small_flag = 0;
float big = 2.0f, small=0.5f;

//5.1 tiger 그리기

//tiger object
#define N_TIGER_FRAMES 12
GLuint tiger_VBO, tiger_VAO;
int tiger_n_triangles[N_TIGER_FRAMES];
int tiger_vertex_offset[N_TIGER_FRAMES];
GLfloat* tiger_vertices[N_TIGER_FRAMES];

Material_Parameters material_tiger;

// TO DO
void prepare_tiger_20171273(void) {
	/* fill your code here */

	int i, n_bytes_per_vertex, n_bytes_per_triangle, tiger_n_total_triangles = 0;
	char filename[512];

	n_bytes_per_vertex = 8 * sizeof(float); // 3 for vertex, 3 for normal, and 2 for texcoord
	n_bytes_per_triangle = 3 * n_bytes_per_vertex;

	for (i = 0; i < N_TIGER_FRAMES; i++) {
		sprintf(filename, "Data/Tiger_%d%d_triangles_vnt.geom", i / 10, i % 10);
		tiger_n_triangles[i] = read_geometry(&tiger_vertices[i], n_bytes_per_triangle, filename);
		// Assume all geometry files are effective.
		tiger_n_total_triangles += tiger_n_triangles[i];

		if (i == 0)
			tiger_vertex_offset[i] = 0;
		else
			tiger_vertex_offset[i] = tiger_vertex_offset[i - 1] + 3 * tiger_n_triangles[i - 1];
	}

	// Initialize vertex buffer object.
	glGenBuffers(1, &tiger_VBO);

	glBindBuffer(GL_ARRAY_BUFFER, tiger_VBO);
	glBufferData(GL_ARRAY_BUFFER, tiger_n_total_triangles * n_bytes_per_triangle, NULL, GL_STATIC_DRAW);

	for (i = 0; i < N_TIGER_FRAMES; i++)
		glBufferSubData(GL_ARRAY_BUFFER, tiger_vertex_offset[i] * n_bytes_per_vertex,
			tiger_n_triangles[i] * n_bytes_per_triangle, tiger_vertices[i]);

	// As the geometry data exists now in graphics memory, ...
	for (i = 0; i < N_TIGER_FRAMES; i++)
		free(tiger_vertices[i]);

	// Initialize vertex array object.
	glGenVertexArrays(1, &tiger_VAO);
	glBindVertexArray(tiger_VAO);

	glBindBuffer(GL_ARRAY_BUFFER, tiger_VBO);
	glVertexAttribPointer(LOC_VERTEX, 3, GL_FLOAT, GL_FALSE, n_bytes_per_vertex, BUFFER_OFFSET(0));
	glEnableVertexAttribArray(0);
	glVertexAttribPointer(LOC_NORMAL, 3, GL_FLOAT, GL_FALSE, n_bytes_per_vertex, BUFFER_OFFSET(3 * sizeof(float)));
	glEnableVertexAttribArray(1);
	glVertexAttribPointer(LOC_TEXCOORD, 2, GL_FLOAT, GL_FALSE, n_bytes_per_vertex, BUFFER_OFFSET(6 * sizeof(float)));
	glEnableVertexAttribArray(2);

	glBindBuffer(GL_ARRAY_BUFFER, 0);
	glBindVertexArray(0);

	material_tiger.ambient_color[0] = 0.24725f;
	material_tiger.ambient_color[1] = 0.1995f;
	material_tiger.ambient_color[2] = 0.0745f;
	material_tiger.ambient_color[3] = 1.0f;

	material_tiger.diffuse_color[0] = 0.75164f;
	material_tiger.diffuse_color[1] = 0.60648f;
	material_tiger.diffuse_color[2] = 0.22648f;
	material_tiger.diffuse_color[3] = 1.0f;

	material_tiger.specular_color[0] = 0.728281f;
	material_tiger.specular_color[1] = 0.655802f;
	material_tiger.specular_color[2] = 0.466065f;
	material_tiger.specular_color[3] = 1.0f;

	material_tiger.specular_exponent = 51.2f;

	material_tiger.emissive_color[0] = 0.1f;
	material_tiger.emissive_color[1] = 0.1f;
	material_tiger.emissive_color[2] = 0.0f;
	material_tiger.emissive_color[3] = 1.0f;

	glHint(GL_GENERATE_MIPMAP_HINT, GL_NICEST);

	glActiveTexture(GL_TEXTURE0 + TEXTURE_ID_TIGER);
	glBindTexture(GL_TEXTURE_2D, texture_names[TEXTURE_ID_TIGER]);

	My_glTexImage2D_from_file("Data/Texture1.jpg");

	glGenerateMipmap(GL_TEXTURE_2D);

	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);

	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);
}

void set_material_tiger(void) {
	// assume ShaderProgram_TXPS is used
	glUniform4fv(loc_material.ambient_color, 1, material_tiger.ambient_color);
	glUniform4fv(loc_material.diffuse_color, 1, material_tiger.diffuse_color);
	glUniform4fv(loc_material.specular_color, 1, material_tiger.specular_color);
	glUniform1f(loc_material.specular_exponent, material_tiger.specular_exponent);
	glUniform4fv(loc_material.emissive_color, 1, material_tiger.emissive_color);
}

void draw_tiger_20171273(void) {
	/* fill your code here */
	glUseProgram(h_ShaderProgram_TXPS);

	glFrontFace(GL_CW);

	glUniform1i(loc_primitive_color, TEXTURE_ID_TIGER);

	if (rotation_angle_tiger <= 90) {
		ModelViewMatrix = glm::translate(ViewMatrix, glm::vec3(1500.0f - rotation_angle_tiger * (2700.0f / 90.0f), 3600.0f - rotation_angle_tiger * (3600.0f / 90.0f), 0.0f));
		ModelViewMatrix = glm::rotate(ModelViewMatrix, -32.0f * TO_RADIAN, glm::vec3(0.0f, 0.0f, 1.0f));
		ModelViewMatrix = glm::scale(ModelViewMatrix, glm::vec3(2.5f, 2.5f, 2.5f));
	}
	else if (rotation_angle_tiger <= 180) {
		ModelViewMatrix = glm::rotate(ViewMatrix, (rotation_angle_tiger - 90.0f) * TO_RADIAN, glm::vec3(0.0f, 0.0f, 1.0f));
		ModelViewMatrix = glm::translate(ModelViewMatrix, glm::vec3(-1200.0f + 350.0f * (rotation_angle_tiger - 90.0f) / 90.0f, 0.0f, 0.0f));
		ModelViewMatrix = glm::scale(ModelViewMatrix, glm::vec3(2.5f, 2.5f, 2.5f));
	}
	else if (rotation_angle_tiger <= 270) {
		ModelViewMatrix = glm::translate(ViewMatrix, glm::vec3(0.0f + 3600.0f * (rotation_angle_tiger - 180.0f) / 90.0f, -850.0f - 1250.0f * (rotation_angle_tiger - 180.0f) / 90.0f, 0.0f));
		ModelViewMatrix = glm::rotate(ModelViewMatrix, 60.0f * TO_RADIAN, glm::vec3(0.0f, 0.0f, 1.0f));
		ModelViewMatrix = glm::scale(ModelViewMatrix, glm::vec3(2.5f, 2.5f, 2.5f));
	}

	ModelViewProjectionMatrix = ProjectionMatrix * ModelViewMatrix;
	ModelViewMatrixInvTrans = glm::inverseTranspose(glm::mat3(ModelViewMatrix));
	glUniformMatrix4fv(loc_ModelViewProjectionMatrix_TXPS, 1, GL_FALSE, &ModelViewProjectionMatrix[0][0]);
	glUniformMatrix4fv(loc_ModelViewMatrix_TXPS, 1, GL_FALSE, &ModelViewMatrix[0][0]);
	glUniformMatrix3fv(loc_ModelViewMatrixInvTrans_TXPS, 1, GL_FALSE, &ModelViewMatrixInvTrans[0][0]);

	glBindVertexArray(tiger_VAO);
	glDrawArrays(GL_TRIANGLES, tiger_vertex_offset[cur_frame_tiger], 3 * tiger_n_triangles[cur_frame_tiger]);
	glBindVertexArray(0);

	glUseProgram(0);
}

//4.0.1 spider 그리기

// spider object
#define N_SPIDER_FRAMES 16
GLuint spider_VBO, spider_VAO;
int spider_n_triangles[N_SPIDER_FRAMES];
int spider_vertex_offset[N_SPIDER_FRAMES];
GLfloat* spider_vertices[N_SPIDER_FRAMES];

Material_Parameters material_spider;

void prepare_spider_20171273(void) {
	int i, n_bytes_per_vertex, n_bytes_per_triangle, spider_n_total_triangles = 0;
	char filename[512];

	n_bytes_per_vertex = 8 * sizeof(float); // 3 for vertex, 3 for normal, and 2 for texcoord
	n_bytes_per_triangle = 3 * n_bytes_per_vertex;

	for (i = 0; i < N_SPIDER_FRAMES; i++) {
		sprintf(filename, "Data/dynamic_objects/spider/spider_vnt_%d%d.geom", i / 10, i % 10);
		spider_n_triangles[i] = read_geometry(&spider_vertices[i], n_bytes_per_triangle, filename);
		// assume all geometry files are effective
		spider_n_total_triangles += spider_n_triangles[i];

		if (i == 0)
			spider_vertex_offset[i] = 0;
		else
			spider_vertex_offset[i] = spider_vertex_offset[i - 1] + 3 * spider_n_triangles[i - 1];
	}

	// initialize vertex buffer object
	glGenBuffers(1, &spider_VBO);

	glBindBuffer(GL_ARRAY_BUFFER, spider_VBO);
	glBufferData(GL_ARRAY_BUFFER, spider_n_total_triangles * n_bytes_per_triangle, NULL, GL_STATIC_DRAW);

	for (i = 0; i < N_SPIDER_FRAMES; i++)
		glBufferSubData(GL_ARRAY_BUFFER, spider_vertex_offset[i] * n_bytes_per_vertex,
			spider_n_triangles[i] * n_bytes_per_triangle, spider_vertices[i]);

	// as the geometry data exists now in graphics memory, ...
	for (i = 0; i < N_SPIDER_FRAMES; i++)
		free(spider_vertices[i]);

	// initialize vertex array object
	glGenVertexArrays(1, &spider_VAO);
	glBindVertexArray(spider_VAO);

	glBindBuffer(GL_ARRAY_BUFFER, spider_VBO);
	glVertexAttribPointer(LOC_VERTEX, 3, GL_FLOAT, GL_FALSE, n_bytes_per_vertex, BUFFER_OFFSET(0));
	glEnableVertexAttribArray(0);
	glVertexAttribPointer(LOC_NORMAL, 3, GL_FLOAT, GL_FALSE, n_bytes_per_vertex, BUFFER_OFFSET(3 * sizeof(float)));
	glEnableVertexAttribArray(1);
	glVertexAttribPointer(LOC_TEXCOORD, 2, GL_FLOAT, GL_FALSE, n_bytes_per_vertex, BUFFER_OFFSET(6 * sizeof(float)));
	glEnableVertexAttribArray(2);

	glBindBuffer(GL_ARRAY_BUFFER, 0);
	glBindVertexArray(0);

	glHint(GL_GENERATE_MIPMAP_HINT, GL_NICEST);

	glActiveTexture(GL_TEXTURE0 + TEXTURE_ID_TIGER);
	glBindTexture(GL_TEXTURE_2D, texture_names[TEXTURE_ID_TIGER]);

	My_glTexImage2D_from_file("Data/dynamic_objects/tiger/tiger_tex2.jpg");

	glGenerateMipmap(GL_TEXTURE_2D);

	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);

	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);
}

void draw_spider_20171273(void) {
	glUseProgram(h_ShaderProgram_TXPS);

	glFrontFace(GL_CW);

	glUniform3f(loc_primitive_color, 1.0f, 0.0f, 1.0f);

	if (jump_flag == 0) {
		if (rotation_angle_spider < 180) {
			ModelViewMatrix = glm::rotate(ViewMatrix, rotation_angle_spider * TO_RADIAN, glm::vec3(0.0f, 0.0f, 1.0f));
			ModelViewMatrix = glm::translate(ModelViewMatrix, glm::vec3(0.0f, 800.0f, 0.0f));
			ModelViewMatrix = glm::rotate(ModelViewMatrix, 90.0f * TO_RADIAN, glm::vec3(0.0f, 0.0f, 1.0f));
			ModelViewMatrix = glm::rotate(ModelViewMatrix, -90.0f * TO_RADIAN, glm::vec3(1.0f, 0.0f, 0.0f));
			ModelViewMatrix = glm::scale(ModelViewMatrix, glm::vec3(200.0f, 200.0f, 200.0f));
		}
		else if (rotation_angle_spider < 360) {
			ModelViewMatrix = glm::rotate(ViewMatrix, -(rotation_angle_spider - 180.0f) * TO_RADIAN, glm::vec3(0.0f, 0.0f, 1.0f));
			ModelViewMatrix = glm::translate(ModelViewMatrix, glm::vec3(0.0f, -800.0f, 0.0f));
			ModelViewMatrix = glm::rotate(ModelViewMatrix, 90.0f * TO_RADIAN, glm::vec3(0.0f, 0.0f, 1.0f));
			ModelViewMatrix = glm::rotate(ModelViewMatrix, -90.0f * TO_RADIAN, glm::vec3(1.0f, 0.0f, 0.0f));
			ModelViewMatrix = glm::scale(ModelViewMatrix, glm::vec3(200.0f, 200.0f, 200.0f));
		}
	}
	else if (jump_flag == 1) {
		if (rotation_angle_spider < 180) {
			ModelViewMatrix = glm::translate(ViewMatrix, glm::vec3(0.0f, 0.0f, 720.0f - 3*rotation_angle_spider));
			ModelViewMatrix = glm::rotate(ModelViewMatrix, rotation_angle_spider * TO_RADIAN, glm::vec3(0.0f, 0.0f, 1.0f));
			ModelViewMatrix = glm::translate(ModelViewMatrix, glm::vec3(0.0f, 800.0f, 0.0f));
			ModelViewMatrix = glm::rotate(ModelViewMatrix, 90.0f * TO_RADIAN, glm::vec3(0.0f, 0.0f, 1.0f));
			ModelViewMatrix = glm::rotate(ModelViewMatrix, -90.0f * TO_RADIAN, glm::vec3(1.0f, 0.0f, 0.0f));
			ModelViewMatrix = glm::scale(ModelViewMatrix, glm::vec3(200.0f, 200.0f, 200.0f));
		}
		else if (rotation_angle_spider < 360) {
			ModelViewMatrix = glm::translate(ViewMatrix, glm::vec3(0.0f, 0.0f, 720.0f - 3*(rotation_angle_spider - 180.0f)));
			ModelViewMatrix = glm::rotate(ModelViewMatrix, -(rotation_angle_spider - 180.0f) * TO_RADIAN, glm::vec3(0.0f, 0.0f, 1.0f));
			ModelViewMatrix = glm::translate(ModelViewMatrix, glm::vec3(0.0f, -800.0f, 0.0f));
			ModelViewMatrix = glm::rotate(ModelViewMatrix, 90.0f * TO_RADIAN, glm::vec3(0.0f, 0.0f, 1.0f));
			ModelViewMatrix = glm::rotate(ModelViewMatrix, -90.0f * TO_RADIAN, glm::vec3(1.0f, 0.0f, 0.0f));
			ModelViewMatrix = glm::scale(ModelViewMatrix, glm::vec3(200.0f, 200.0f, 200.0f));
		}
		if (rotation_angle_spider == 0.0f || rotation_angle_spider == 180.0f) {
			jump_flag = 0;
		}
	}

	ModelViewProjectionMatrix = ProjectionMatrix * ModelViewMatrix;
	ModelViewMatrixInvTrans = glm::inverseTranspose(glm::mat3(ModelViewMatrix));
	glUniformMatrix4fv(loc_ModelViewProjectionMatrix_TXPS, 1, GL_FALSE, &ModelViewProjectionMatrix[0][0]);
	glUniformMatrix4fv(loc_ModelViewMatrix_TXPS, 1, GL_FALSE, &ModelViewMatrix[0][0]);
	glUniformMatrix3fv(loc_ModelViewMatrixInvTrans_TXPS, 1, GL_FALSE, &ModelViewMatrixInvTrans[0][0]);


	glBindVertexArray(spider_VAO);
	glDrawArrays(GL_TRIANGLES, spider_vertex_offset[cur_frame_spider], 3 * spider_n_triangles[cur_frame_spider]);
	glBindVertexArray(0);

	glUseProgram(0);
}

//4.0.1 wolf 그리기

// wolf object
#define N_WOLF_FRAMES 17
GLuint wolf_VBO, wolf_VAO;
int wolf_n_triangles[N_WOLF_FRAMES];
int wolf_vertex_offset[N_WOLF_FRAMES];
GLfloat* wolf_vertices[N_WOLF_FRAMES];

Material_Parameters material_wolf;

void prepare_wolf_20171273(void) {
	int i, n_bytes_per_vertex, n_bytes_per_triangle, wolf_n_total_triangles = 0;
	char filename[512];

	n_bytes_per_vertex = 8 * sizeof(float); // 3 for vertex, 3 for normal, and 2 for texcoord
	n_bytes_per_triangle = 3 * n_bytes_per_vertex;

	for (i = 0; i < N_WOLF_FRAMES; i++) {
		sprintf(filename, "Data/dynamic_objects/wolf/wolf_%02d_vnt.geom", i);
		wolf_n_triangles[i] = read_geometry(&wolf_vertices[i], n_bytes_per_triangle, filename);
		// assume all geometry files are effective
		wolf_n_total_triangles += wolf_n_triangles[i];

		if (i == 0)
			wolf_vertex_offset[i] = 0;
		else
			wolf_vertex_offset[i] = wolf_vertex_offset[i - 1] + 3 * wolf_n_triangles[i - 1];
	}

	// initialize vertex buffer object
	glGenBuffers(1, &wolf_VBO);

	glBindBuffer(GL_ARRAY_BUFFER, wolf_VBO);
	glBufferData(GL_ARRAY_BUFFER, wolf_n_total_triangles * n_bytes_per_triangle, NULL, GL_STATIC_DRAW);

	for (i = 0; i < N_WOLF_FRAMES; i++)
		glBufferSubData(GL_ARRAY_BUFFER, wolf_vertex_offset[i] * n_bytes_per_vertex,
			wolf_n_triangles[i] * n_bytes_per_triangle, wolf_vertices[i]);

	// as the geometry data exists now in graphics memory, ...
	for (i = 0; i < N_WOLF_FRAMES; i++)
		free(wolf_vertices[i]);

	// initialize vertex array object
	glGenVertexArrays(1, &wolf_VAO);
	glBindVertexArray(wolf_VAO);

	glBindBuffer(GL_ARRAY_BUFFER, wolf_VBO);
	glVertexAttribPointer(LOC_VERTEX, 3, GL_FLOAT, GL_FALSE, n_bytes_per_vertex, BUFFER_OFFSET(0));
	glEnableVertexAttribArray(0);
	glVertexAttribPointer(LOC_NORMAL, 3, GL_FLOAT, GL_FALSE, n_bytes_per_vertex, BUFFER_OFFSET(3 * sizeof(float)));
	glEnableVertexAttribArray(1);
	glVertexAttribPointer(LOC_TEXCOORD, 2, GL_FLOAT, GL_FALSE, n_bytes_per_vertex, BUFFER_OFFSET(6 * sizeof(float)));
	glEnableVertexAttribArray(2);

	glBindBuffer(GL_ARRAY_BUFFER, 0);
	glBindVertexArray(0);

	glHint(GL_GENERATE_MIPMAP_HINT, GL_NICEST);

	glActiveTexture(GL_TEXTURE0 + TEXTURE_ID_TIGER);
	glBindTexture(GL_TEXTURE_2D, texture_names[TEXTURE_ID_TIGER]);

	My_glTexImage2D_from_file("Data/dynamic_objects/tiger/tiger_tex2.jpg");

	glGenerateMipmap(GL_TEXTURE_2D);

	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);

	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);
}

void draw_wolf_20171273(void) {
	glUseProgram(h_ShaderProgram_TXPS);

	glFrontFace(GL_CW);

	glUniform3f(loc_primitive_color, 1.0f, 1.0f, 0.0f);

	ModelViewMatrix = glm::translate(ViewMatrix, glm::vec3(4465.0f, -2600.0f, 0.0f));
	ModelViewMatrix = glm::rotate(ModelViewMatrix, -rotation_angle_wolf * TO_RADIAN, glm::vec3(0.0f, 0.0f, 1.0f));
	ModelViewMatrix = glm::translate(ModelViewMatrix, glm::vec3(0.0f, -1000.0f, 0.0f));
	ModelViewMatrix = glm::rotate(ModelViewMatrix, -90.0f * TO_RADIAN, glm::vec3(0.0f, 0.0f, 1.0f));
	ModelViewMatrix = glm::rotate(ModelViewMatrix, 90.0f * TO_RADIAN, glm::vec3(1.0f, 0.0f, 0.0f));
	for (int i = 0; i < big_flag; i++) {
		ModelViewMatrix = glm::scale(ModelViewMatrix, glm::vec3(big, big, big));
	}
	for (int i = 0; i < small_flag; i++) {
		ModelViewMatrix = glm::scale(ModelViewMatrix, glm::vec3(small, small, small));
	}
	ModelViewMatrix = glm::scale(ModelViewMatrix, glm::vec3(400.0f, 400.0f, 400.0f));
	ModelViewProjectionMatrix = ProjectionMatrix * ModelViewMatrix;
	ModelViewMatrixInvTrans = glm::inverseTranspose(glm::mat3(ModelViewMatrix));
	glUniformMatrix4fv(loc_ModelViewProjectionMatrix_TXPS, 1, GL_FALSE, &ModelViewProjectionMatrix[0][0]);
	glUniformMatrix4fv(loc_ModelViewMatrix_TXPS, 1, GL_FALSE, &ModelViewMatrix[0][0]);
	glUniformMatrix3fv(loc_ModelViewMatrixInvTrans_TXPS, 1, GL_FALSE, &ModelViewMatrixInvTrans[0][0]);

	glBindVertexArray(wolf_VAO);
	glDrawArrays(GL_TRIANGLES, wolf_vertex_offset[cur_frame_wolf], 3 * wolf_n_triangles[cur_frame_wolf]);
	glBindVertexArray(0);

	glUseProgram(0);
}

//4.0.1 dragon 두마리 그리기

// dragon object
GLuint dragon_VBO, dragon_VAO;
int dragon_n_triangles;
GLfloat* dragon_vertices;

Material_Parameters material_dragon;

void prepare_dragon_20171273(void) {
	int i, n_bytes_per_vertex, n_bytes_per_triangle, dragon_n_total_triangles = 0;
	char filename[512];

	n_bytes_per_vertex = 8 * sizeof(float); // 3 for vertex, 3 for normal, and 2 for texcoord
	n_bytes_per_triangle = 3 * n_bytes_per_vertex;

	sprintf(filename, "Data/static_objects/dragon_vnt.geom");
	dragon_n_triangles = read_geometry(&dragon_vertices, n_bytes_per_triangle, filename);
	// assume all geometry files are effective
	dragon_n_total_triangles += dragon_n_triangles;


	// initialize vertex buffer object
	glGenBuffers(1, &dragon_VBO);

	glBindBuffer(GL_ARRAY_BUFFER, dragon_VBO);
	glBufferData(GL_ARRAY_BUFFER, dragon_n_total_triangles * 3 * n_bytes_per_vertex, dragon_vertices, GL_STATIC_DRAW);

	// as the geometry data exists now in graphics memory, ...
	free(dragon_vertices);

	// initialize vertex array object
	glGenVertexArrays(1, &dragon_VAO);
	glBindVertexArray(dragon_VAO);

	glBindBuffer(GL_ARRAY_BUFFER, dragon_VBO);
	glVertexAttribPointer(LOC_VERTEX, 3, GL_FLOAT, GL_FALSE, n_bytes_per_vertex, BUFFER_OFFSET(0));
	glEnableVertexAttribArray(0);
	glVertexAttribPointer(LOC_NORMAL, 3, GL_FLOAT, GL_FALSE, n_bytes_per_vertex, BUFFER_OFFSET(3 * sizeof(float)));
	glEnableVertexAttribArray(1);
	glVertexAttribPointer(LOC_TEXCOORD, 2, GL_FLOAT, GL_FALSE, n_bytes_per_vertex, BUFFER_OFFSET(6 * sizeof(float)));
	glEnableVertexAttribArray(2);

	glBindBuffer(GL_ARRAY_BUFFER, 0);
	glBindVertexArray(0);

	glHint(GL_GENERATE_MIPMAP_HINT, GL_NICEST);

	glActiveTexture(GL_TEXTURE0 + TEXTURE_ID_TIGER);
	glBindTexture(GL_TEXTURE_2D, texture_names[TEXTURE_ID_TIGER]);

	My_glTexImage2D_from_file("Data/dynamic_objects/tiger/tiger_tex2.jpg");

	glGenerateMipmap(GL_TEXTURE_2D);

	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);

	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);
}

void draw_dragon1_20171273(void) {
	glUseProgram(h_ShaderProgram_TXPS);

	glFrontFace(GL_CW);

	glUniform3f(loc_primitive_color, 1.0f, 1.0f, 0.0f);

	ModelViewMatrix = glm::translate(ViewMatrix, glm::vec3(4465.0f, -2600.0f, 0.0f));
	ModelViewMatrix = glm::translate(ModelViewMatrix, glm::vec3(1750.0f, 100.0f, 1680.0f));
	ModelViewMatrix = glm::rotate(ModelViewMatrix, 180.0f * TO_RADIAN, glm::vec3(0.0f, 0.0f, 1.0f));
	ModelViewMatrix = glm::scale(ModelViewMatrix, glm::vec3(30.0f, 30.0f, 30.0f));
	ModelViewProjectionMatrix = ProjectionMatrix * ModelViewMatrix;
	ModelViewMatrixInvTrans = glm::inverseTranspose(glm::mat3(ModelViewMatrix));
	glUniformMatrix4fv(loc_ModelViewProjectionMatrix_TXPS, 1, GL_FALSE, &ModelViewProjectionMatrix[0][0]);
	glUniformMatrix4fv(loc_ModelViewMatrix_TXPS, 1, GL_FALSE, &ModelViewMatrix[0][0]);
	glUniformMatrix3fv(loc_ModelViewMatrixInvTrans_TXPS, 1, GL_FALSE, &ModelViewMatrixInvTrans[0][0]);

	glBindVertexArray(dragon_VAO);
	glDrawArrays(GL_TRIANGLES, 0, 3 * dragon_n_triangles);
	glBindVertexArray(0);

	glUseProgram(0);
}

void draw_dragon2_20171273(void) {
	glUseProgram(h_ShaderProgram_TXPS);

	glFrontFace(GL_CW);

	glUniform3f(loc_primitive_color, 1.0f, 1.0f, 0.0f);

	ModelViewMatrix = glm::translate(ViewMatrix, glm::vec3(4465.0f, -2600.0f, 0.0f));
	ModelViewMatrix = glm::translate(ModelViewMatrix, glm::vec3(1450.0f, -1500.0f, 1680.0f));
	ModelViewMatrix = glm::rotate(ModelViewMatrix, 180.0f * TO_RADIAN, glm::vec3(0.0f, 0.0f, 1.0f));
	ModelViewMatrix = glm::scale(ModelViewMatrix, glm::vec3(30.0f, 30.0f, 30.0f));
	ModelViewProjectionMatrix = ProjectionMatrix * ModelViewMatrix;
	ModelViewMatrixInvTrans = glm::inverseTranspose(glm::mat3(ModelViewMatrix));
	glUniformMatrix4fv(loc_ModelViewProjectionMatrix_TXPS, 1, GL_FALSE, &ModelViewProjectionMatrix[0][0]);
	glUniformMatrix4fv(loc_ModelViewMatrix_TXPS, 1, GL_FALSE, &ModelViewMatrix[0][0]);
	glUniformMatrix3fv(loc_ModelViewMatrixInvTrans_TXPS, 1, GL_FALSE, &ModelViewMatrixInvTrans[0][0]);

	glBindVertexArray(dragon_VAO);
	glDrawArrays(GL_TRIANGLES, 0, 3 * dragon_n_triangles);
	glBindVertexArray(0);
}

//4.0.1 optimus 2개 그리기

// optimus object
GLuint optimus_VBO, optimus_VAO;
int optimus_n_triangles;
GLfloat* optimus_vertices;

Material_Parameters material_optimus;

void prepare_optimus_20171273(void) {
	int i, n_bytes_per_vertex, n_bytes_per_triangle, optimus_n_total_triangles = 0;
	char filename[512];

	n_bytes_per_vertex = 8 * sizeof(float); // 3 for vertex, 3 for normal, and 2 for texcoord
	n_bytes_per_triangle = 3 * n_bytes_per_vertex;

	sprintf(filename, "Data/static_objects/optimus_vnt.geom");
	optimus_n_triangles = read_geometry(&optimus_vertices, n_bytes_per_triangle, filename);
	// assume all geometry files are effective
	optimus_n_total_triangles += optimus_n_triangles;


	// initialize vertex buffer object
	glGenBuffers(1, &optimus_VBO);

	glBindBuffer(GL_ARRAY_BUFFER, optimus_VBO);
	glBufferData(GL_ARRAY_BUFFER, optimus_n_total_triangles * 3 * n_bytes_per_vertex, optimus_vertices, GL_STATIC_DRAW);

	// as the geometry data exists now in graphics memory, ...
	free(optimus_vertices);

	// initialize vertex array object
	glGenVertexArrays(1, &optimus_VAO);
	glBindVertexArray(optimus_VAO);

	glBindBuffer(GL_ARRAY_BUFFER, optimus_VBO);
	glVertexAttribPointer(LOC_VERTEX, 3, GL_FLOAT, GL_FALSE, n_bytes_per_vertex, BUFFER_OFFSET(0));
	glEnableVertexAttribArray(0);
	glVertexAttribPointer(LOC_NORMAL, 3, GL_FLOAT, GL_FALSE, n_bytes_per_vertex, BUFFER_OFFSET(3 * sizeof(float)));
	glEnableVertexAttribArray(1);
	glVertexAttribPointer(LOC_TEXCOORD, 2, GL_FLOAT, GL_FALSE, n_bytes_per_vertex, BUFFER_OFFSET(6 * sizeof(float)));
	glEnableVertexAttribArray(2);

	glBindBuffer(GL_ARRAY_BUFFER, 0);
	glBindVertexArray(0);

	glHint(GL_GENERATE_MIPMAP_HINT, GL_NICEST);

	glActiveTexture(GL_TEXTURE0 + TEXTURE_ID_TIGER);
	glBindTexture(GL_TEXTURE_2D, texture_names[TEXTURE_ID_TIGER]);

	My_glTexImage2D_from_file("Data/Texture2.jpg");

	glGenerateMipmap(GL_TEXTURE_2D);

	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);

	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);
}

void draw_optimus1_20171273(void) {
	glUseProgram(h_ShaderProgram_TXPS);

	glFrontFace(GL_CW);

	glUniform3f(loc_primitive_color, 1.0f, 1.0f, 0.0f);

	ModelViewMatrix = glm::translate(ViewMatrix, glm::vec3(3465.0f, -1600.0f, 0.0f));
	ModelViewMatrix = glm::rotate(ModelViewMatrix, -100.0f * TO_RADIAN, glm::vec3(0.0f, 0.0f, 1.0f));
	ModelViewMatrix = glm::scale(ModelViewMatrix, glm::vec3(0.8f, 0.8f, 0.8f));
	ModelViewProjectionMatrix = ProjectionMatrix * ModelViewMatrix;
	ModelViewMatrixInvTrans = glm::inverseTranspose(glm::mat3(ModelViewMatrix));
	glUniformMatrix4fv(loc_ModelViewProjectionMatrix_TXPS, 1, GL_FALSE, &ModelViewProjectionMatrix[0][0]);
	glUniformMatrix4fv(loc_ModelViewMatrix_TXPS, 1, GL_FALSE, &ModelViewMatrix[0][0]);
	glUniformMatrix3fv(loc_ModelViewMatrixInvTrans_TXPS, 1, GL_FALSE, &ModelViewMatrixInvTrans[0][0]);

	glBindVertexArray(optimus_VAO);
	glDrawArrays(GL_TRIANGLES, 0, 3 * optimus_n_triangles);
	glBindVertexArray(0);
}

void draw_optimus2_20171273(void) {
	glUseProgram(h_ShaderProgram_TXPS);

	glFrontFace(GL_CW);

	glUniform3f(loc_primitive_color, 1.0f, 1.0f, 0.0f);

	ModelViewMatrix = glm::translate(ViewMatrix, glm::vec3(3400.0f, -2500.0f, 0.0f));
	ModelViewMatrix = glm::rotate(ModelViewMatrix, 80.0f * TO_RADIAN, glm::vec3(0.0f, 0.0f, 1.0f));
	ModelViewMatrix = glm::scale(ModelViewMatrix, glm::vec3(0.8f, 0.8f, 0.8f));
	ModelViewProjectionMatrix = ProjectionMatrix * ModelViewMatrix;
	ModelViewMatrixInvTrans = glm::inverseTranspose(glm::mat3(ModelViewMatrix));
	glUniformMatrix4fv(loc_ModelViewProjectionMatrix_TXPS, 1, GL_FALSE, &ModelViewProjectionMatrix[0][0]);
	glUniformMatrix4fv(loc_ModelViewMatrix_TXPS, 1, GL_FALSE, &ModelViewMatrix[0][0]);
	glUniformMatrix3fv(loc_ModelViewMatrixInvTrans_TXPS, 1, GL_FALSE, &ModelViewMatrixInvTrans[0][0]);

	glBindVertexArray(optimus_VAO);
	glDrawArrays(GL_TRIANGLES, 0, 3 * optimus_n_triangles);
	glBindVertexArray(0);
}

//4.0.1 cow 1개 그리기

// cow object
GLuint cow_VBO, cow_VAO;
int cow_n_triangles;
GLfloat* cow_vertices;

Material_Parameters material_cow;

void prepare_cow_20171273(void) {
	int i, n_bytes_per_vertex, n_bytes_per_triangle, cow_n_total_triangles = 0;
	char filename[512];

	n_bytes_per_vertex = 8 * sizeof(float); // 3 for vertex, 3 for normal, and 2 for texcoord
	n_bytes_per_triangle = 3 * n_bytes_per_vertex;

	sprintf(filename, "Data/static_objects/cow_vn.geom");
	cow_n_triangles = read_geometry(&cow_vertices, n_bytes_per_triangle, filename);
	// assume all geometry files are effective
	cow_n_total_triangles += cow_n_triangles;


	// initialize vertex buffer object
	glGenBuffers(1, &cow_VBO);

	glBindBuffer(GL_ARRAY_BUFFER, cow_VBO);
	glBufferData(GL_ARRAY_BUFFER, cow_n_total_triangles * 3 * n_bytes_per_vertex, cow_vertices, GL_STATIC_DRAW);

	// as the geometry data exists now in graphics memory, ...
	free(cow_vertices);

	// initialize vertex array object
	glGenVertexArrays(1, &cow_VAO);
	glBindVertexArray(cow_VAO);

	glBindBuffer(GL_ARRAY_BUFFER, cow_VBO);
	glVertexAttribPointer(LOC_VERTEX, 3, GL_FLOAT, GL_FALSE, n_bytes_per_vertex, BUFFER_OFFSET(0));
	glEnableVertexAttribArray(0);
	glVertexAttribPointer(LOC_NORMAL, 3, GL_FLOAT, GL_FALSE, n_bytes_per_vertex, BUFFER_OFFSET(3 * sizeof(float)));
	glEnableVertexAttribArray(1);

	glBindBuffer(GL_ARRAY_BUFFER, 0);
	glBindVertexArray(0);
}

void draw_cow_20171273(void) {
	glUseProgram(h_ShaderProgram_TXPS);

	glFrontFace(GL_CW);

	glUniform3f(loc_primitive_color, 1.0f, 1.0f, 0.0f);

	ModelViewMatrix = glm::translate(ViewMatrix, glm::vec3(-400.0f, 0.0f, 100.0f));
	ModelViewMatrix = glm::rotate(ModelViewMatrix, 180.0f * TO_RADIAN, glm::vec3(0.0f, 0.0f, 1.0f));
	ModelViewMatrix = glm::rotate(ModelViewMatrix, 90.0f * TO_RADIAN, glm::vec3(1.0f, 0.0f, 0.0f));
	ModelViewMatrix = glm::scale(ModelViewMatrix, glm::vec3(400.0f, 400.0f, 400.0f));
	ModelViewProjectionMatrix = ProjectionMatrix * ModelViewMatrix;
	ModelViewMatrixInvTrans = glm::inverseTranspose(glm::mat3(ModelViewMatrix));
	glUniformMatrix4fv(loc_ModelViewProjectionMatrix_TXPS, 1, GL_FALSE, &ModelViewProjectionMatrix[0][0]);
	glUniformMatrix4fv(loc_ModelViewMatrix_TXPS, 1, GL_FALSE, &ModelViewMatrix[0][0]);
	glUniformMatrix3fv(loc_ModelViewMatrixInvTrans_TXPS, 1, GL_FALSE, &ModelViewMatrixInvTrans[0][0]);

	glBindVertexArray(cow_VAO);
	glDrawArrays(GL_TRIANGLES, 0, 3 * cow_n_triangles);
	glBindVertexArray(0);
}

//
/*****************************  END: geometry setup *****************************/

/********************  START: callback function definitions *********************/
void display(void) {
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	
	draw_grid();
	draw_axes();
	draw_bistro_exterior();
	set_material_tiger();
	draw_tiger_20171273();//tiger 그리기
	//set_material_tiger();
	//draw_spider_20171273();//spider 그리기
	//set_material_tiger();
	//draw_wolf_20171273();//wolf 그리기
	//set_material_tiger();
	//draw_dragon1_20171273();//dragon1 그리기
	//draw_dragon2_20171273();//dragon2 그리기
	set_material_tiger();
	draw_optimus1_20171273();//optimus1 그리기
	//draw_optimus2_20171273();//optimus2 그리기
	//set_material_tiger();
	//draw_cow_20171273();//cow 그리기

	glutSwapBuffers();
}

//time 함수
void timer_scene_tiger(int value) {
	timestamp_scene_tiger = (timestamp_scene_tiger + 1 % UINT_MAX);
	cur_frame_tiger = timestamp_scene_tiger % N_TIGER_FRAMES;
	rotation_angle_tiger = (timestamp_scene_tiger % 270);
	glutPostRedisplay();
	if (move_flag) {
		glutTimerFunc(10, timer_scene_tiger, 0);
	}
}
void timer_scene_spider(int value) {
	timestamp_scene_spider = (timestamp_scene_spider + 1 % UINT_MAX);
	cur_frame_spider = timestamp_scene_spider % N_SPIDER_FRAMES;
	rotation_angle_spider = (timestamp_scene_spider % 360);
	glutPostRedisplay();
	glutTimerFunc(10, timer_scene_spider, 0);
}
void timer_scene_wolf(int value) {
	timestamp_scene_wolf = (timestamp_scene_wolf + 1 % UINT_MAX);
	cur_frame_wolf = timestamp_scene_wolf % N_SPIDER_FRAMES;
	rotation_angle_wolf = (timestamp_scene_wolf % 360);
	glutPostRedisplay();
	glutTimerFunc(10, timer_scene_wolf, 0);
}
//

int camera_flag = 0;
#define CAM_ROT_SENSITIVITY 0.15f

glm::mat4 renew_cam_orientation(float angle, glm::vec3 axis) {
	glm::mat4 RotationMatrix;
	RotationMatrix = glm::mat4(glm::rotate(glm::mat4(1.0), CAM_ROT_SENSITIVITY * TO_RADIAN * angle, axis));
	return RotationMatrix;
}

void keyboard(unsigned char key, int x, int y) {

	static int flag_cull_face = 0;
	static int PRP_distance_level = 0;
	static int flag_floor_mag_filter = 0, flag_floor_min_filter = 0;
	static int flag_tiger_mag_filter = 0, flag_tiger_min_filter = 0;

	glm::vec4 position_EC;
	glm::vec3 direction_EC;

	if ((key >= '0') && (key <= '0' + NUMBER_OF_LIGHT_SUPPORTED - 1)) {
		int light_ID = (int)(key - '0');

		glUseProgram(h_ShaderProgram_TXPS);
		light[light_ID].light_on = 1 - light[light_ID].light_on;
		glUniform1i(loc_light[light_ID].light_on, light[light_ID].light_on);
		glUseProgram(0);

		glutPostRedisplay();
		return;
	}

	switch (key) {
	case 'f':
		b_draw_grid = b_draw_grid ? false : true;
		glutPostRedisplay();
		break;
	case '1':
		set_current_camera(CAMERA_0);
		camera_flag = 0;
		glutPostRedisplay();
		break;
	case '2':
		set_current_camera(CAMERA_1);
		camera_flag = 1;
		glutPostRedisplay();
		break;
	case '3':
		set_current_camera(CAMERA_2);
		camera_flag = 2;
		glutPostRedisplay();
		break;
	case '4':
		set_current_camera(CAMERA_3);
		camera_flag = 3;
		glutPostRedisplay();
		break;
	case '5':
		set_current_camera(CAMERA_m);
		camera_flag = 4;
		glutPostRedisplay();
		break;
	case 't':
		set_current_camera(CAMERA_t);
		camera_flag = 5;
		if (camera_flag == 5) {
			if (rotation_angle_tiger <= 90) {
				ViewMatrix = glm::rotate(ViewMatrix, 32.0f * TO_RADIAN, glm::vec3(0.0f, 0.0f, 1.0f));
				ViewMatrix = glm::translate(ViewMatrix, -glm::vec3(1500.0f - rotation_angle_tiger * (2700.0f / 90.0f), 3600.0f - rotation_angle_tiger * (3600.0f / 90.0f), 0.0f));
				ViewMatrix = ViewMatrix * 2.5f;
			}
			else if (rotation_angle_tiger <= 180) {
				ViewMatrix = glm::translate(ViewMatrix, -glm::vec3(-1200.0f + 350.0f * (rotation_angle_tiger - 90.0f) / 90.0f, 0.0f, 0.0f));
				ViewMatrix = glm::rotate(ViewMatrix, -(rotation_angle_tiger - 90.0f) * TO_RADIAN, glm::vec3(0.0f, 0.0f, 1.0f));
				ViewMatrix = ViewMatrix * 2.5f;
			}
			else if (rotation_angle_tiger <= 270) {
				ViewMatrix = glm::rotate(ViewMatrix, -60.0f * TO_RADIAN, glm::vec3(0.0f, 0.0f, 1.0f));
				ViewMatrix = glm::translate(ViewMatrix, -glm::vec3(0.0f + 3600.0f * (rotation_angle_tiger - 180.0f) / 90.0f, -850.0f - 1250.0f * (rotation_angle_tiger - 180.0f) / 90.0f, 0.0f));
				ViewMatrix = ViewMatrix * 2.5f;
			}
			ModelViewProjectionMatrix = ProjectionMatrix * ModelViewMatrix;
		}
		glutPostRedisplay();
		break;
	case 'g':
		set_current_camera(CAMERA_g);
		camera_flag = 6;
		if (camera_flag == 6) {
			if (rotation_angle_tiger <= 90) {
				ViewMatrix = glm::rotate(ViewMatrix, 32.0f * TO_RADIAN, glm::vec3(0.0f, 0.0f, 1.0f));
				ViewMatrix = glm::translate(ViewMatrix, -glm::vec3(1500.0f - rotation_angle_tiger * (2700.0f / 90.0f), 3600.0f - rotation_angle_tiger * (3600.0f / 90.0f), 0.0f));
				ViewMatrix = ViewMatrix * 2.5f;
			}
			else if (rotation_angle_tiger <= 180) {
				ViewMatrix = glm::translate(ViewMatrix, -glm::vec3(-1200.0f + 350.0f * (rotation_angle_tiger - 90.0f) / 90.0f, 0.0f, 0.0f));
				ViewMatrix = glm::rotate(ViewMatrix, -(rotation_angle_tiger - 90.0f) * TO_RADIAN, glm::vec3(0.0f, 0.0f, 1.0f));
				ViewMatrix = ViewMatrix * 2.5f;
			}
			else if (rotation_angle_tiger <= 270) {
				ViewMatrix = glm::rotate(ViewMatrix, -60.0f * TO_RADIAN, glm::vec3(0.0f, 0.0f, 1.0f));
				ViewMatrix = glm::translate(ViewMatrix, -glm::vec3(0.0f + 3600.0f * (rotation_angle_tiger - 180.0f) / 90.0f, -850.0f - 1250.0f * (rotation_angle_tiger - 180.0f) / 90.0f, 0.0f));
				ViewMatrix = ViewMatrix * 2.5f;
			}
			ModelViewProjectionMatrix = ProjectionMatrix * ModelViewMatrix;
		}
		glutPostRedisplay();
		break;
	case 27: // ESC key
		glutLeaveMainLoop(); // Incur destuction callback for cleanups.
		break;
	//호랑이 움직임 멈추기
	case 's':
		move_flag = 1 - move_flag;
		if (move_flag == 1) {
			glutTimerFunc(100, timer_scene_tiger, 0);
		}
		else if (move_flag == 0) {
			break;
		}
		break;
	//spider 점프
	case 'j':
		if (jump_flag == 0) {
			jump_flag = 1;
		}
		break;
	//wolf 크기 키우기
	case 'b':
		big_flag += 1;
		break;
	//wolf 크기 줄이기
	case 'n':
		small_flag += 1;
		break;
	case 'w':
		int light_ID = 1;

		glUseProgram(h_ShaderProgram_TXPS);
		light[light_ID].light_on = 1 - light[light_ID].light_on;
		glUniform1i(loc_light[light_ID].light_on, light[light_ID].light_on);
		glUseProgram(0);

		glutPostRedisplay();
		break;
	}
}

#define CAM_TSPEED 3.0f

//카메라 줌인 줌아웃을 위한 wheelfunc
void mouseWheel(int button, int dir, int x, int y) {
	//wheel up
	if ((glutGetModifiers() == GLUT_ACTIVE_SHIFT) && dir > 0) {
		camera_info[camera_flag].zoom -= CAM_TSPEED;
		ProjectionMatrix = glm::perspective(camera_info[camera_flag].zoom * camera_info[camera_flag].fovy * TO_RADIAN, camera_info[camera_flag].aspect_ratio, camera_info[camera_flag].near_c, camera_info[camera_flag].far_c);
		ViewProjectionMatrix = ProjectionMatrix * ViewMatrix;
		glutPostRedisplay();
	}
	//wheel down
	else if ((glutGetModifiers() == GLUT_ACTIVE_SHIFT) && dir <= 0) {
		camera_info[camera_flag].zoom += CAM_TSPEED;
		ProjectionMatrix = glm::perspective(camera_info[camera_flag].zoom * camera_info[camera_flag].fovy * TO_RADIAN, camera_info[camera_flag].aspect_ratio, camera_info[camera_flag].near_c, camera_info[camera_flag].far_c);
		ViewProjectionMatrix = ProjectionMatrix * ViewMatrix;
		glutPostRedisplay();
	}
}

#define CAM_POS 300.0f

void special(int key, int x, int y) {
	if (camera_flag == 4) {
		if ((glutGetModifiers() == GLUT_ACTIVE_SHIFT) && key == GLUT_KEY_UP) {
			ViewMatrix = glm::translate(ViewMatrix, glm::vec3(0.0f, -CAM_POS, 0.0f));
			ViewProjectionMatrix = ProjectionMatrix * ViewMatrix;
		}
		else if ((glutGetModifiers() == GLUT_ACTIVE_SHIFT) && key == GLUT_KEY_DOWN) {
			ViewMatrix = glm::translate(ViewMatrix, glm::vec3(0.0f, CAM_POS, 0.0f));
			ViewProjectionMatrix = ProjectionMatrix * ViewMatrix;
		}
		else if ((glutGetModifiers() == GLUT_ACTIVE_SHIFT) && key == GLUT_KEY_LEFT) {
			ViewMatrix = glm::translate(ViewMatrix, glm::vec3(CAM_POS, 0.0f, 0.0f));
			ViewProjectionMatrix = ProjectionMatrix * ViewMatrix;
		}
		else if ((glutGetModifiers() == GLUT_ACTIVE_SHIFT) && key == GLUT_KEY_RIGHT) {
			ViewMatrix = glm::translate(ViewMatrix, glm::vec3(-CAM_POS, 0.0f, 0.0f));
			ViewProjectionMatrix = ProjectionMatrix * ViewMatrix;
		}
		else if ((glutGetModifiers() == GLUT_ACTIVE_SHIFT) && key == GLUT_KEY_PAGE_DOWN) {
			ViewMatrix = glm::translate(ViewMatrix, glm::vec3(0.0f, 0.0f, CAM_POS));
			ViewProjectionMatrix = ProjectionMatrix * ViewMatrix;
		}
		else if ((glutGetModifiers() == GLUT_ACTIVE_SHIFT) && key == GLUT_KEY_PAGE_UP) {
			ViewMatrix = glm::translate(ViewMatrix, glm::vec3(0.0f, 0.0f, -CAM_POS));
			ViewProjectionMatrix = ProjectionMatrix * ViewMatrix;
		}
	}
	glutPostRedisplay();
}

unsigned int leftbutton_pressed = 0;
int prevx, prevy;

void mousepress(int button, int state, int x, int y) {
	if ((button == GLUT_LEFT_BUTTON) && (state == GLUT_DOWN)) {
		prevx = x, prevy = y;
		leftbutton_pressed = 1;
		glutPostRedisplay();
	}
	else if ((button == GLUT_LEFT_BUTTON) && (state == GLUT_UP)) {
		leftbutton_pressed = 0;
		glutPostRedisplay();
	}
}

void motion(int x, int y) {
	if (camera_flag == 4) {
	
		float delx, dely;

		if ((glutGetModifiers() == GLUT_ACTIVE_SHIFT) && leftbutton_pressed) {
			delx = (float)(x - prevx), dely = -(float)(y - prevy);
			prevx = x, prevy = y;

			ViewMatrix = glm::translate(ViewMatrix, glm::vec3(0.0f, 1.0f, 0.0f));
			ViewMatrix = renew_cam_orientation(-delx, glm::vec3(0.0f, 1.0f, 0.0f)) * ViewMatrix;
			ViewMatrix = glm::translate(ViewMatrix, -glm::vec3(0.0f, 1.0f, 0.0f));

			ViewMatrix = glm::translate(ViewMatrix, glm::vec3(1.0f, 0.0f, 0.0f));
			ViewMatrix = renew_cam_orientation(-dely, glm::vec3(1.0f, 0.0f, 0.0f)) * ViewMatrix;
			ViewMatrix = glm::translate(ViewMatrix, -glm::vec3(1.0f, 0.0f, 0.0f));

			ViewProjectionMatrix = ProjectionMatrix * ViewMatrix;
			glutPostRedisplay();
		}
	}
}

void reshape(int width, int height) {
	float aspect_ratio;

	glViewport(0, 0, width, height);

	camera_info[camera_flag].aspect_ratio = (float)width / height;
	ProjectionMatrix = glm::perspective(camera_info[camera_flag].zoom * camera_info[camera_flag].fovy, camera_info[camera_flag].aspect_ratio, camera_info[camera_flag].near_c, camera_info[camera_flag].far_c);
	ViewProjectionMatrix = ProjectionMatrix * ViewMatrix;
	glutPostRedisplay();
}

void cleanup(void) {
	glDeleteVertexArrays(1, &axes_VAO);
	glDeleteBuffers(1, &axes_VBO);

	glDeleteVertexArrays(1, &grid_VAO);
	glDeleteBuffers(1, &grid_VBO);

	glDeleteVertexArrays(scene.n_materials, bistro_exterior_VAO);
	glDeleteBuffers(scene.n_materials, bistro_exterior_VBO);

	//tiger clean
	glDeleteVertexArrays(1, &tiger_VAO);
	glDeleteBuffers(1, &tiger_VBO);

	//spider clean
	glDeleteVertexArrays(1, &spider_VAO);
	glDeleteBuffers(1, &spider_VBO);

	//wolf clean
	glDeleteVertexArrays(1, &wolf_VAO);
	glDeleteBuffers(1, &wolf_VBO);

	glDeleteTextures(scene.n_textures, bistro_exterior_texture_names);

	free(bistro_exterior_n_triangles);
	free(bistro_exterior_vertex_offset);

	free(bistro_exterior_VAO);
	free(bistro_exterior_VBO);

	free(bistro_exterior_texture_names);
	free(flag_texture_mapping);
}
/*********************  END: callback function definitions **********************/

void register_callbacks(void) {
	glutDisplayFunc(display);
	glutKeyboardFunc(keyboard);
	glutMouseWheelFunc(mouseWheel);
	glutSpecialFunc(special);
	glutMouseFunc(mousepress);
	glutMotionFunc(motion);
	glutReshapeFunc(reshape);
	//tiger time
	glutTimerFunc(100, timer_scene_tiger, 0);
	//spider time
	glutTimerFunc(100, timer_scene_spider, 0);
	//spider time
	glutTimerFunc(100, timer_scene_wolf, 0);
	glutCloseFunc(cleanup);
}

void initialize_OpenGL(void) {
	glEnable(GL_DEPTH_TEST);
	glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);
	glClearColor(0.0f, 0.0f, 0.0f, 1.0f);

	ViewMatrix = glm::mat4(1.0f);
	ProjectionMatrix = glm::mat4(1.0f);
	ViewProjectionMatrix = ProjectionMatrix * ViewMatrix;

	initialize_lights_and_material();
	initialize_flags();
}

void set_up_scene_lights(void) {
	// point_light_EC: use light 0
	light[0].light_on = 1;
	light[0].position[0] = 0.0f; light[0].position[1] = 100.0f; 	// point light position in EC
	light[0].position[2] = 0.0f; light[0].position[3] = 1.0f;

	light[0].ambient_color[0] = 0.13f; light[0].ambient_color[1] = 0.13f;
	light[0].ambient_color[2] = 0.13f; light[0].ambient_color[3] = 1.0f;

	light[0].diffuse_color[0] = 0.5f; light[0].diffuse_color[1] = 0.5f;
	light[0].diffuse_color[2] = 0.5f; light[0].diffuse_color[3] = 1.5f;

	light[0].specular_color[0] = 0.8f; light[0].specular_color[1] = 0.8f;
	light[0].specular_color[2] = 0.8f; light[0].specular_color[3] = 1.0f;

	// spot_light_WC: use light 1
	light[1].light_on = 1;
	light[1].position[0] = 0.0f; light[1].position[1] = 2000.0f; // spot light position in WC
	light[1].position[2] = 0.0f; light[1].position[3] = 1.0f;

	light[1].ambient_color[0] = 0.152f; light[1].ambient_color[1] = 0.152f;
	light[1].ambient_color[2] = 0.152f; light[1].ambient_color[3] = 1.0f;

	light[1].diffuse_color[0] = 0.572f; light[1].diffuse_color[1] = 0.572f;
	light[1].diffuse_color[2] = 0.572f; light[1].diffuse_color[3] = 1.0f;

	light[1].specular_color[0] = 0.772f; light[1].specular_color[1] = 0.772f;
	light[1].specular_color[2] = 0.772f; light[1].specular_color[3] = 1.0f;

	light[1].spot_direction[0] = 0.0f; light[1].spot_direction[1] = -1.0f; // spot light direction in WC
	light[1].spot_direction[2] = 0.0f;
	light[1].spot_cutoff_angle = 60.0f;
	light[1].spot_exponent = 100.0f;

	light[2].light_on = 1;
	light[2].position[0] = 0.0f; light[2].position[1] = 2000.0f; // spot light position in WC
	light[2].position[2] = 0.0f; light[2].position[3] = 1.0f;

	light[2].ambient_color[0] = 0.152f; light[2].ambient_color[1] = 0.152f;
	light[2].ambient_color[2] = 0.152f; light[2].ambient_color[3] = 1.0f;

	light[2].diffuse_color[0] = 0.572f; light[2].diffuse_color[1] = 0.572f;
	light[2].diffuse_color[2] = 0.572f; light[2].diffuse_color[3] = 1.0f;

	light[2].specular_color[0] = 0.772f; light[2].specular_color[1] = 0.772f;
	light[2].specular_color[2] = 0.772f; light[2].specular_color[3] = 1.0f;

	light[2].spot_direction[0] = 0.0f; light[2].spot_direction[1] = -1.0f; // spot light direction in WC
	light[2].spot_direction[2] = 0.0f;
	light[2].spot_cutoff_angle = 60.0f;
	light[2].spot_exponent = 100.0f;

	glUseProgram(h_ShaderProgram_TXPS);
	glUniform1i(loc_light[0].light_on, light[0].light_on);
	glUniform4fv(loc_light[0].position, 1, light[0].position);
	glUniform4fv(loc_light[0].ambient_color, 1, light[0].ambient_color);
	glUniform4fv(loc_light[0].diffuse_color, 1, light[0].diffuse_color);
	glUniform4fv(loc_light[0].specular_color, 1, light[0].specular_color);

	glUniform1i(loc_light[1].light_on, light[1].light_on);
	// need to supply position in EC for shading
	glm::vec4 position_EC1 = ViewMatrix * glm::vec4(light[1].position[0], light[1].position[1],
		light[1].position[2], light[1].position[3]);
	glUniform4fv(loc_light[1].position, 1, &position_EC1[0]);
	glUniform4fv(loc_light[1].ambient_color, 1, light[1].ambient_color);
	glUniform4fv(loc_light[1].diffuse_color, 1, light[1].diffuse_color);
	glUniform4fv(loc_light[1].specular_color, 1, light[1].specular_color);
	// need to supply direction in EC for shading in this example shader
	// note that the viewing transform is a rigid body transform
	// thus transpose(inverse(mat3(ViewMatrix)) = mat3(ViewMatrix)
	glm::vec3 direction_EC1 = glm::mat3(ViewMatrix) * glm::vec3(light[1].spot_direction[0], light[1].spot_direction[1],
		light[1].spot_direction[2]);
	glUniform3fv(loc_light[1].spot_direction, 1, &direction_EC1[0]);
	glUniform1f(loc_light[1].spot_cutoff_angle, light[1].spot_cutoff_angle);
	glUniform1f(loc_light[1].spot_exponent, light[1].spot_exponent);

	glUseProgram(0);
}

void prepare_scene(void) {
	prepare_axes();
	prepare_grid();
	prepare_bistro_exterior();
	//prepare objects
	prepare_tiger_20171273();
	//prepare_spider_20171273();
	//prepare_wolf_20171273();
	//prepare_dragon_20171273();
	prepare_optimus_20171273();
	//prepare_cow_20171273();
	set_up_scene_lights();
}

void initialize_renderer(void) {
	register_callbacks();
	prepare_shader_program();
	initialize_OpenGL();
	prepare_scene();
	initialize_camera();
}

void initialize_glew(void) {
	GLenum error;

	glewExperimental = GL_TRUE;

	error = glewInit();
	if (error != GLEW_OK) {
		fprintf(stderr, "Error: %s\n", glewGetErrorString(error));
		exit(-1);
	}
	fprintf(stdout, "********************************************************************************\n");
	fprintf(stdout, " - GLEW version supported: %s\n", glewGetString(GLEW_VERSION));
	fprintf(stdout, " - OpenGL renderer: %s\n", glGetString(GL_RENDERER));
	fprintf(stdout, " - OpenGL version supported: %s\n", glGetString(GL_VERSION));
	fprintf(stdout, "********************************************************************************\n\n");
}

void print_message(const char* m) {
	fprintf(stdout, "%s\n\n", m);
}

void greetings(char* program_name, char messages[][256], int n_message_lines) {
	fprintf(stdout, "********************************************************************************\n\n");
	fprintf(stdout, "  PROGRAM NAME: %s\n\n", program_name);
	fprintf(stdout, "    This program was coded for CSE4170 students\n");
	fprintf(stdout, "      of Dept. of Comp. Sci. & Eng., Sogang University.\n\n");

	for (int i = 0; i < n_message_lines; i++)
		fprintf(stdout, "%s\n", messages[i]);
	fprintf(stdout, "\n********************************************************************************\n\n");

	initialize_glew();
}

#define N_MESSAGE_LINES 9
void drawScene(int argc, char* argv[]) {
	char program_name[64] = "Sogang CSE4170 Bistro Exterior Scene";
	char messages[N_MESSAGE_LINES][256] = { 
		"    - Keys used:",
		"		'f' : draw x, y, z axes and grid",
		"		'1' : set the camera for original view",
		"		'2' : set the camera for bistro view",
		"		'3' : set the camera for tree view",	
		"		'4' : set the camera for top view",
		"		'5' : set the camera for front view",
		"		'6' : set the camera for side view",
		"		'ESC' : program close",
	};

	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH);
	glutInitWindowSize(900, 600);
	glutInitWindowPosition(20, 20);
	glutInitContextVersion(3, 3);
	glutInitContextProfile(GLUT_CORE_PROFILE);
	glutCreateWindow(program_name);

	greetings(program_name, messages, N_MESSAGE_LINES);
	initialize_renderer();

	glutSetOption(GLUT_ACTION_ON_WINDOW_CLOSE, GLUT_ACTION_GLUTMAINLOOP_RETURNS);
	glutMainLoop();
}
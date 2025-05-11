from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
import os

load_dotenv()

@CrewBase
class ResearchAi():
    """ResearchAi crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            verbose=True,
            # llm=self.ollama_1b
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'],
            verbose=True,
            # llm=self.phi3
        )
        
    @agent
    def methods_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['methods_analyst'],
            verbose=True
        )

    @agent
    def literature_survey_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['literature_survey_agent'],
            verbose=True
        )

    @agent
    def research_problem_formulator(self) -> Agent:
        return Agent(
            config=self.agents_config['research_problem_formulator'],
            verbose=True
        )

    @agent
    def paper_classifier(self) -> Agent:
        return Agent(
            config=self.agents_config['paper_classifier'],
            verbose=True
        )

    @agent
    def summarization_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['summarization_agent'],
            verbose=True
        )

    @agent
    def qa_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['qa_agent'],
            verbose=True
        )

    @agent
    def report_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['report_generator'],
            verbose=True
        )

    @agent
    def data_extractor(self) -> Agent:
        return Agent(
            config=self.agents_config['data_extractor'],
            verbose=True
        )

    @agent
    def timeline_planner(self) -> Agent:
        return Agent(
            config=self.agents_config['timeline_planner'],
            verbose=True
        )

    @agent
    def experimental_designer(self) -> Agent:
        return Agent(
            config=self.agents_config['experimental_designer'],
            verbose=True
        )

    @agent
    def citation_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['citation_manager'],
            verbose=True
        )

    @agent
    def thesis_structurer(self) -> Agent:
        return Agent(
            config=self.agents_config['thesis_structurer'],
            verbose=True
        )

    @agent
    def presentation_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['presentation_generator'],
            verbose=True
        )

    @agent
    def multilingual_translator(self) -> Agent:
        return Agent(
            config=self.agents_config['multilingual_translator'],
            verbose=True
        )

    @agent
    def plagiarism_checker(self) -> Agent:
        return Agent(
            config=self.agents_config['plagiarism_checker'],
            verbose=True
        )

    @agent
    def knowledge_graph_builder(self) -> Agent:
        return Agent(
            config=self.agents_config['knowledge_graph_builder'],
            verbose=True
        )

    @agent
    def agent_orchestrator(self) -> Agent:
        return Agent(
            config=self.agents_config['agent_orchestrator'],
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'],
            output_file='output_file/report.md'
        )
        
    @task
    def methods_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['methods_analysis_task'],
            output_file='output_file/methods_analysis.md'
        )

    @task
    def literature_survey_task(self) -> Task:
        return Task(
            config=self.tasks_config['literature_survey_task'],
            output_file='output_file/literature_survey.md'
        )

    @task
    def research_problem_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_problem_task'],
            output_file='output_file/research_problem.md'
        )

    @task
    def paper_classification_task(self) -> Task:
        return Task(
            config=self.tasks_config['paper_classification_task'],
            output_file='output_file/paper_classification.md'
        )

    @task
    def summarization_task(self) -> Task:
        return Task(
            config=self.tasks_config['summarization_task'],
            output_file='output_file/summaries.md'
        )

    @task
    def qa_task(self) -> Task:
        return Task(
            config=self.tasks_config['qa_task'],
            output_file='output_file/qa_responses.md'
        )

    @task
    def report_generation_task(self) -> Task:
        return Task(
            config=self.tasks_config['report_generation_task'],
            output_file='output_file/research_report.md'
        )

    @task
    def data_extraction_task(self) -> Task:
        return Task(
            config=self.tasks_config['data_extraction_task'],
            output_file='output_file/extracted_data.md'
        )

    @task
    def timeline_planning_task(self) -> Task:
        return Task(
            config=self.tasks_config['timeline_planning_task'],
            output_file='output_file/research_timeline.md'
        )

    @task
    def experimental_design_task(self) -> Task:
        return Task(
            config=self.tasks_config['experimental_design_task'],
            output_file='output_file/experimental_design.md'
        )

    @task
    def citation_management_task(self) -> Task:
        return Task(
            config=self.tasks_config['citation_management_task'],
            output_file='output_file/citations.bib'
        )

    @task
    def thesis_structuring_task(self) -> Task:
        return Task(
            config=self.tasks_config['thesis_structuring_task'],
            output_file='output_file/thesis_structure.md'
        )

    @task
    def presentation_generation_task(self) -> Task:
        return Task(
            config=self.tasks_config['presentation_generation_task'],
            output_file='output_file/presentation.md'
        )

    @task
    def translation_task(self) -> Task:
        return Task(
            config=self.tasks_config['translation_task'],
            output_file='output_file/translations.md'
        )

    @task
    def plagiarism_check_task(self) -> Task:
        return Task(
            config=self.tasks_config['plagiarism_check_task'],
            output_file='output_file/plagiarism_report.md'
        )

    @task
    def knowledge_graph_task(self) -> Task:
        return Task(
            config=self.tasks_config['knowledge_graph_task'],
            output_file='output_file/knowledge_graph.md'
        )

    @task
    def orchestration_task(self) -> Task:
        return Task(
            config=self.tasks_config['orchestration_task'],
            output_file='output_file/workflow_status.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ResearchAi crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )

The research focuses on how mental health can be understood through analyzing people’s posts on social media platforms. Many people openly share personal struggles on social media, so this study aimed to identify clues about mental health from these posts.
We develop a dataset, which is a collection of posts from BeyondBlue, Australia's most well-known and trusted mental health organization, labeled with four different categories related to well-being.
- The dataset is publicly available for use at: - [Mental Health data for Wellness Dimensions analysis](https://huggingface.co/datasets/hebashakeel/Bert-classification-wellness)
- We based our work on Halbert L. Dunn’s theory, which breaks down wellness into multiple dimensions, or “aspects” of life, that together impact a person’s well-being.
- Physical Aspect (PA): This includes anything related to physical health, such as body image, sleep, diet, or issues like fatigue and illness.
- Intellectual and Vocational Aspect (IVA): This covers personal growth, education, job satisfaction, or any struggles related to school, work, or learning.
- Social Aspect (SA): This aspect includes social relationships and interactions with others, like family, friendships, and feelings of belonging or isolation.
- Spiritual and Emotional Aspect (SEA): This includes emotions, life purpose, and inner peace, focusing on whether someone feels fulfilled or is struggling with sadness, anxiety, or hopelessness.

- The models used include popular ones like BERT, RoBERTa, MentalBERT. Each of these models has its strengths: BERT and RoBERTa: These are “encoder-only” models, which means they’re good at understanding text and making sense of context. MentalBERT: This version of BERT is specially trained on mental health data, making it particularly useful for analyzing mental health-related posts.



# Links to the related papers: 

- [DepressionEmo: A novel dataset for multilabel classification of depression emotions](https://arxiv.org/pdf/2401.04655)
- [WELLXPLAIN: Wellness Concept Extraction and Classification in Reddit Posts for Mental Health Analysis](https://arxiv.org/pdf/2308.13710)
- [GitHub for WellnessData](https://github.com/drmuskangarg/WellnessDimensions)
